"""Specialized to_bytes methods for specific types"""
import datetime
import inspect
import math
import types
from datetime import date

from qsum.core.constants import FILE_IO_CHUNK_SIZE
from qsum.data.to_bytes import bytes_from_repr, str_to_bytes


def int_to_bytes(obj: int) -> bytes:
    """Convert int's in to the most compact byte representation possible

    CURRENTLY UNUSED, while cleverly packing integers tightly it's actually ~5x slower then just calling repr

    Args:
        obj: integer to convert to bytes

    Returns:
        bytes representing integer
    """
    return obj.to_bytes(1 if obj == 0 else math.floor((math.log2(abs(obj)) + 1) / 8 + 1), byteorder='big', signed=True)


def complex_to_bytes(obj) -> bytes:
    """
    Custom logic for converting complex numbers to bytes which handles the oddities around -0.0 and 0.0

    Args:
        obj: complex object to convert to bytes

    Returns:
        bytes representing the complex object
    """

    real, imag = obj.real, obj.imag
    # this line might seem odd, but think about -0.0 (which equals 0.0),
    new_complex = complex(0.0 if real == 0.0 else real, 0.0 if imag == 0.0 else imag)

    return bytes_from_repr(new_complex)


def module_to_bytes(obj: types.ModuleType) -> bytes:
    """Initial implementation will change every time the source code of the module source code changes

    Args:
        obj: module to convert to bytes

    Returns:
        byes representing the function
    """
    source_code = inspect.getsource(obj)
    return source_code.encode()


def _file_to_bytes_generator(obj):
    """A generator to read the lines of a file"
    Args:
        obj: file handle to iterate
    Returns:
        The full bytes of a file while preserving the original position
    """
    # store the original position
    org_position = obj.tell()
    # start at the beginning of the file
    obj.seek(0)
    while True:
        # if the file is in reading bytes mode return the bytes directly otherwise encode the string to bytes
        # note we never read lines as the line separator should be included even when reading text files
        chunk = obj.read(FILE_IO_CHUNK_SIZE) if obj.mode == 'rb' else obj.read(FILE_IO_CHUNK_SIZE).encode()

        if len(chunk) == 0:
            break
        yield chunk
    # restore the original position
    obj.seek(org_position)


def file_to_bytes(obj) -> bytes:
    """Extract the bytes of a file, but do not include the path itself in the bytes

    Args:
        obj: file to extract the bytes of

    Returns:
        Generator that extracts all the bytes of a file
    """
    return _file_to_bytes_generator(obj)


def date_to_bytes(obj: date) -> bytes:
    """Convert a date in to bytes
    Args:
        obj: date to convert in to bytes
    Returns:
        bytes representing the date
    """
    # if you're wondering about the spaces here, remove them and run test_unique_date_bytes
    return str_to_bytes("{} {} {}".format(obj.year, obj.month, obj.day))


def datetime_to_bytes(obj: datetime) -> bytes:
    """Convert a datetime in to bytes
    Args:
        obj: datetime to convert in to bytes
    Returns:
        bytes representing the datetime
    """
    # use seconds since epoc in order to properly compare different time zones
    # https://docs.python.org/3.8/library/datetime.html#datetime.datetime.timestamp
    # we trust this to be a well behaved float (not swapping 0.0 for -0.0, so use bytes_from_repr directly
    return bytes_from_repr(obj.timestamp())
