import hashlib


def data_checksum(obj, obj_type):
    """Generate a checksum for the object data

    Args:
        obj:
        obj_type:

    Returns:

    """
    hasher = hashlib.sha256()
    hasher.update(repr(obj).encode())
    return hasher.digest()
