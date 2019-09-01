import hashlib

from qsum.data.type_map import TYPE_TO_BINARY_FUNCTION


def data_checksum(obj, obj_type):
    """Generate a checksum for the object data

    Args:
        obj:
        obj_type:

    Returns:

    """
    hasher = hashlib.sha256()
    binary_data_func = TYPE_TO_BINARY_FUNCTION[obj_type]
    hasher.update(binary_data_func(obj))
    return hasher.digest()
