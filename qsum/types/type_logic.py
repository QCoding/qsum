from qsum.core.constants import ChecksumType, CHECKSUM_CLASS_NAME
from qsum.core.exceptions import QSumInvalidTypeException, QSumInvalidPrefixException, QSumInvalidChecksum
from qsum.types.type_map import PREFIX_BYTES, TYPE_TO_PREFIX, PREFIX_TO_TYPE, UNREGISTERED_TYPE_PREFIX


def all_prefix_types():
    """All valid prefix types"""
    return TYPE_TO_PREFIX.keys()


def type_to_prefix(obj_type, allow_unregistered: bool = True) -> bytes:
    """Coverts a type to two byte prefix

    Args:
        obj_type: type of the object
        allow_unregistered: if True provide a generic key for unregistered types

    Returns:
        prefix representing the type

    """
    try:
        return TYPE_TO_PREFIX[obj_type]
    except KeyError as err:
        if allow_unregistered:
            return UNREGISTERED_TYPE_PREFIX
        raise QSumInvalidTypeException("{} type does not have a registered type".format(obj_type)) from err


def prefix_to_type(type_prefix: bytes) -> type:
    """Converts a two byte prefix to a type"""
    try:
        return PREFIX_TO_TYPE[type_prefix]
    except KeyError as err:
        raise QSumInvalidPrefixException("{} is not a valid prefix".format(type_prefix)) from err


def checksum_to_type(checksum: ChecksumType):
    """Extract the prefix bytes from the checksum and lookup the type"""
    if isinstance(checksum, bytes):
        return prefix_to_type(checksum[:PREFIX_BYTES])
    if isinstance(checksum, str):
        # if hex then the type prefix is twice as long
        return prefix_to_type(bytes.fromhex(checksum[:PREFIX_BYTES * 2]))
    if type(checksum).__name__ == CHECKSUM_CLASS_NAME:
        return prefix_to_type(checksum.checksum_bytes[:PREFIX_BYTES])
    raise QSumInvalidChecksum("{} is not a valid checksum type".format(checksum))
