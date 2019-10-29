import hashlib
import typing

from qsum.core.constants import HashAlgoType
from qsum.core.exceptions import QSumInvalidDataTypeException, QSumInvalidChecksum
from qsum.data.data_type_map import TYPE_TO_BYTES_FUNCTION
from qsum.types.type_map import PREFIX_BYTES


def all_data_types():
    """Return all of the data types available"""
    return TYPE_TO_BYTES_FUNCTION.keys()


def resolve_hash_algo(hash_algo: HashAlgoType) -> typing.Callable:
    """Resolve the hash_algo to a callable function

    Args:
        hash_algo: a str of a method in hashlib or the callable itself

    Returns:
        a callable hash_algo

    >>> resolve_hash_algo('md5')
    <built-in function openssl_md5>
    >>> resolve_hash_algo(hashlib.md5)
    <built-in function openssl_md5>
    """
    if isinstance(hash_algo, str):
        return getattr(hashlib, hash_algo)
    return hash_algo


def bytes_to_digest(bytes_data: typing.Union[bytes, bytearray], hash_algo: HashAlgoType) -> bytes:
    """Convert bytes in to message digest using the given hash algo

    Args:
        bytes_data:
        hash_algo:  the hash algorithm to use to convert the bytes to a message digest

    Returns:

    """
    hasher = resolve_hash_algo(hash_algo)()
    hasher.update(bytes_data)
    return hasher.digest()


def data_checksum(obj: typing.Any, obj_type, hash_algo: HashAlgoType) -> bytes:
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


def data_digest_from_checksum(checksum: typing.Union[bytes, str]) -> typing.Union[bytes, str]:
    """Extract the data digest bytes from the checksum

    Args:
        checksum: checksum to extra the data digest from

    Returns:
        just the data digest portion of the checksum
    """
    if isinstance(checksum, bytes):
        return checksum[PREFIX_BYTES:]
    if isinstance(checksum, str):
        # if hex then the type prefix is twice as long
        return checksum[PREFIX_BYTES * 2:]
    raise QSumInvalidChecksum("{} is not a valid checksum type".format(checksum))
