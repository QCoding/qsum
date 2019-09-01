import hashlib

from qsum.core.exceptions import QSumInvalidDataTypeException
from qsum.data.type_map import TYPE_TO_BINARY_FUNCTION


def data_checksum(obj, obj_type):
    """Generate a checksum for the object data

    Args:
        obj:
        obj_type:

    Returns:

    """
    hasher = hashlib.sha256()

    # attempt to get the key and raise if we fail to, try and forgive style but raise a nicer exception then KeyError
    try:
        binary_data_func = TYPE_TO_BINARY_FUNCTION[obj_type]
    except KeyError as e:
        raise QSumInvalidDataTypeException("{} is not a recognized checksummable type".format(obj_type)) from e

    hasher.update(binary_data_func(obj))
    return hasher.digest()
