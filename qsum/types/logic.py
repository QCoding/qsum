from qsum.core.exceptions import QSumException
from qsum.types.type_map import PREFIX_BYTES, TYPE_TO_PREFIX, PREFIX_TO_TYPE


class QSumInvalidTypeException(QSumException):
    pass


class QSumInvalidPrefixException(QSumException):
    pass


def type_to_prefix(obj_type):
    try:
        return TYPE_TO_PREFIX[obj_type]
    except KeyError as e:
        raise QSumInvalidTypeException("{} type does not have a registered type".format(obj_type)) from e


def prefix_to_type(type_prefix):
    try:
        return PREFIX_TO_TYPE[type_prefix]
    except KeyError as e:
        raise QSumInvalidPrefixException("{} is not a valid prefix".format(type_prefix)) from e


def checksum_to_type(checksum):
    """Extract the prefix bytes from the checksum and lookup the type"""
    return prefix_to_type(checksum[:PREFIX_BYTES])


def type_checksum(obj_type):
    return type_to_prefix(obj_type)