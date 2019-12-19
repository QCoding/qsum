"""Specialized to_bytes methods for specific types"""
import inspect
import types

from qsum.data.to_bytes import bytes_from_repr


def complex_to_bytes(obj) -> bytes:
    """
    Custom logic for converting complex numbers to bytes which handles the oddities around -0.0 and 0.0

    Args:
        obj: complex object to convert to bytes

    Returns:
        bytes representing the complex object
    """

    real, imag = obj.real, obj.imag
    # this line might seem odd, but think about -0.0 (which equals 0.0),
    new_complex = complex(0.0 if real == 0.0 else real, 0.0 if imag == 0.0 else imag)

    return bytes_from_repr(new_complex)


def function_to_bytes(obj: types.FunctionType) -> bytes:
    """Initial implementation will change every time the source code of the function changes

    Args:
        obj: function to convert in to bytes

    Returns:
        byes representing the funciton
    """
    source_code = inspect.getsource(obj)
    return source_code.encode()
