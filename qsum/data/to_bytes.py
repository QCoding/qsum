"""Functions to convert various types in to bytes that can be hashed"""


def bytes_to_bytes(obj):
    """Identity function"""
    return obj


def str_to_bytes(obj):
    """Convenience method around encode"""
    return obj.encode()


def bytes_from_repr(obj):
    """Encode the repr string of an object in to bytes"""
    return repr(obj).encode()


def float_to_bytes(obj):
    """Check the static float dict and then use a repr_to_bytes style for floats"""
    r = repr(obj)
    # special case to make -0.0 and +0.0 have the same checksum since they are equal
    if r == '-0.0':
        r = '0.0'
    return r.encode()
