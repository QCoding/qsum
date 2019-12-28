import hashlib
import types
import typing

from qsum.core.constants import HashAlgoType, ChecksumType, CHECKSUM_CLASS_NAME
from qsum.core.exceptions import QSumInvalidDataTypeException, QSumInvalidChecksum, QSumInvalidBytesDataType
from qsum.data.data_type_map import TYPE_TO_BYTES_FUNCTION, TYPE_CLASS_TO_BYTES_FUNCTION
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


def bytes_to_digest(bytes_data: typing.Union[bytes, bytearray, typing.Generator], hash_algo: HashAlgoType) -> bytes:
    """Convert bytes in to message digest using the given hash algo

    Args:
        bytes_data: the bytes representing the data or a generator that iterates bytes
        hash_algo:  the hash algorithm to use to convert the bytes to a message digest

    Returns:
        a digest of the bytes
    """
    hasher = resolve_hash_algo(hash_algo)()

    # if given resolved bytes
    if isinstance(bytes_data, (bytes, bytearray)):
        hasher.update(bytes_data)
    # if we have a generator then iterate through it
    elif isinstance(bytes_data, types.GeneratorType):
        for bytes_data_iteration in bytes_data:
            hasher.update(bytes_data_iteration)
    else:
        raise QSumInvalidBytesDataType("'{}' type is not valid for bytes data".format(type(bytes_data)))

    return hasher.digest()


def data_checksum(obj: typing.Any, obj_type, hash_algo: HashAlgoType,
                  checksum_type: typing.Optional[type] = None) -> bytes:
    """Generate a checksum for the object data

    Args:
        obj: object to generate a checksum of
        obj_type: the type of the object or the designed type of object methodology to checksum the data
        hash_algo: the hash algorithm to use to convert the bytes to a message digest
        checksum_type: given this is a data_checksum by default we don't want to include the checksum_type in it,
            but since we support unregistered types and don't them to compare equal, we'll add the type info
            when we know we don't have a 'safe' unique prefix, note type info is not

    Returns:
        a message digest representing the obj

    """

    # attempt to get the key and raise if we fail to, try and forgive style but raise a nicer exception then KeyError
    try:
        bytes_data_func = TYPE_TO_BYTES_FUNCTION[obj_type]
    except KeyError as err:
        raise QSumInvalidDataTypeException("{} is not a recognized checksummable type".format(obj_type)) from err

    # generate the bytes using the custom method
    data_bytes = bytes_data_func(obj)

    if checksum_type is not None:
        # TODO: the great separator debate, is it safe to just add extra bytes here or do we need a unique separator?
        #       in all likelihood we do not, but adding a note in case that decision is ever reversed
        data_bytes += TYPE_CLASS_TO_BYTES_FUNCTION(checksum_type)

    return bytes_to_digest(data_bytes, hash_algo)


def data_digest_from_checksum(checksum: ChecksumType) -> typing.Union[bytes, str]:
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
    if type(checksum).__name__ == CHECKSUM_CLASS_NAME:
        return checksum.checksum_bytes[PREFIX_BYTES:]

    raise QSumInvalidChecksum("{} is not a valid checksum type".format(checksum))
