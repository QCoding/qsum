"""Generic functions to convert various types in to bytes that can be hashed"""
import typing


def bytes_to_bytes(obj) -> bytes:
    """Identity function"""
    return obj


def str_to_bytes(obj) -> bytes:
    """Convenience method around encode"""
    return obj.encode()


def bytes_from_repr(obj) -> bytes:
    """Encode the repr string of an object in to bytes"""
    return repr(obj).encode()


def bytes_from_repr_with_overrides(obj, value_overrides=None, repr_overrides=None) -> bytes:
    """
    bytes_from_repr but with the ability to specify overrides

    Args:
        obj: object to convert to bytes
        value_overrides: if the obj equals a key then override then use the new value to generate the bytes
        repr_overrides: if the repr equals a key key then replace with the value

    Returns:
        the bytes representing the obj
    """
    if value_overrides is not None:
        obj = value_overrides.get(obj, obj)

    obj_repr = repr(obj)

    if repr_overrides is not None:
        obj_repr = repr_overrides.get(obj_repr, obj_repr)

    return obj_repr.encode()


def singleton_to_bytes(obj: typing.Any) -> bytes:
    """ Return a single with 0 value for singleton objects

    Args:
        obj: any singleton object

    Returns: one byte of 0

    """
    return b'\x00'
