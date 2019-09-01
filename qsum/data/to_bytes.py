"""Functions to convert various types in to bytes that can be hashed"""


def str_to_bytes(obj):
    return obj.encode()


def repr_to_bytes(obj):
    return repr(obj).encode()
