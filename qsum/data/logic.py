import hashlib
import typing

from qsum.core.exceptions import QSumInvalidDataTypeException
from qsum.data.type_map import TYPE_TO_BYTES_FUNCTION
from qsum.types.type_map import PREFIX_BYTES


def all_data_types():
    return TYPE_TO_BYTES_FUNCTION.keys()


def bytes_to_digest(bytes_data: typing.Union[bytes, bytearray]) -> bytes:
    hasher = hashlib.sha256()
    hasher.update(bytes_data)
    return hasher.digest()


def data_checksum(obj, obj_type):
    """Generate a checksum for the object data

    Args:
        obj:
        obj_type:

    Returns:

    """

    # attempt to get the key and raise if we fail to, try and forgive style but raise a nicer exception then KeyError
    try:
        bytes_data_func = TYPE_TO_BYTES_FUNCTION[obj_type]
    except KeyError as e:
        raise QSumInvalidDataTypeException("{} is not a recognized checksummable type".format(obj_type)) from e

    return bytes_to_digest(bytes_data_func(obj))


def data_digest_from_checksum(checksum):
    """Extract the data digest bytes from the checksum"""
    return checksum[PREFIX_BYTES:]
