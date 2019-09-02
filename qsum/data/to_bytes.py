"""Functions to convert various types in to bytes that can be hashed"""


def bytes_to_bytes(obj):
    """Identity function"""
    return obj


def str_to_bytes(obj):
    return obj.encode()


def repr_to_bytes(obj):
    return repr(obj).encode()
