import typing

from qsum.core.exceptions import QSumInvalidDataTypeException
from qsum.data.data_type_map import TYPE_TO_BYTES_FUNCTION
from qsum.types.type_map import PREFIX_BYTES


def all_data_types():
    """Return all of the data types available"""
    return TYPE_TO_BYTES_FUNCTION.keys()


def bytes_to_digest(bytes_data: typing.Union[bytes, bytearray], hash_algo) -> bytes:
    """Convert bytes in to message digest using the given hash algo

    Args:
        bytes_data:
        hash_algo:  the hash algorithm to use to convert the bytes to a message digest

    Returns:

    """
    hasher = hash_algo()
    hasher.update(bytes_data)
    return hasher.digest()


def data_checksum(obj: typing.Any, obj_type, hash_algo) -> bytes:
    """Generate a checksum for the object data

    Args:
        obj: object to generate a checksum of
        obj_type: the type of the object or the designed type of object methodology to checksum the data
        hash_algo: the hash algorithm to use to convert the bytes to a message digest

    Returns:
        a message digest representing the obj

    """

    # attempt to get the key and raise if we fail to, try and forgive style but raise a nicer exception then KeyError
    try:
        bytes_data_func = TYPE_TO_BYTES_FUNCTION[obj_type]
    except KeyError as err:
        raise QSumInvalidDataTypeException("{} is not a recognized checksummable type".format(obj_type)) from err

    return bytes_to_digest(bytes_data_func(obj), hash_algo)


def data_digest_from_checksum(checksum) -> bytes:
    """Extract the data digest bytes from the checksum

    Args:
        checksum:

    Returns:
    """
    return checksum[PREFIX_BYTES:]
