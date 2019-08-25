from qsum.core.data import data_checksum
from qsum.core.types import type_checksum


class Checksum(object):
    """Class for decoding and combining checksums"""

    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return self.__value


def checksum(obj, return_type='digest'):
    """Generate a checksum for a given object based on it's type and contents

    Args:
        obj: object to generate a checksum for
        return_type: return_type of the checksum

    Returns:
        string representing a checksum of the object
    """
    # let's just call this once
    obj_type = type(obj)
    return type_checksum(obj_type) + data_checksum(obj, obj_type)
