"""Functions to convert various types in to bytes that can be hashed"""
from qsum.data.to_static import FLOAT_TO_CHECKSUM


def bytes_to_bytes(obj):
    """Identity function"""
    return obj


def str_to_bytes(obj):
    """Convenience method around encode"""
    return obj.encode()


def repr_to_bytes(obj):
    """Encode the repr string of an object in to bytes"""
    return repr(obj).encode()


def float_to_bytes(obj):
    """Check the static float dict and then use a repr_to_bytes style for floats"""
    return FLOAT_TO_CHECKSUM.get(obj, repr_to_bytes(obj))
