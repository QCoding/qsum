from qsum.core.exceptions import QSumInvalidTypeException, QSumInvalidPrefixException
from qsum.types.type_map import PREFIX_BYTES, TYPE_TO_PREFIX, PREFIX_TO_TYPE


def all_prefix_types():
    """All valid prefix types"""
    return TYPE_TO_PREFIX.keys()


def type_to_prefix(obj_type) -> bytes:
    """Coverts a type to two byte prefix"""
    try:
        return TYPE_TO_PREFIX[obj_type]
    except KeyError as err:
        raise QSumInvalidTypeException("{} type does not have a registered type".format(obj_type)) from err


def prefix_to_type(type_prefix) -> type:
    """Converts a two byte prefix to a type"""
    try:
        return PREFIX_TO_TYPE[type_prefix]
    except KeyError as err:
        raise QSumInvalidPrefixException("{} is not a valid prefix".format(type_prefix)) from err


def checksum_to_type(checksum):
    """Extract the prefix bytes from the checksum and lookup the type"""
    return prefix_to_type(checksum[:PREFIX_BYTES])
