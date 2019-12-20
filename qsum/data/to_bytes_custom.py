"""Specialized to_bytes methods for specific types"""
import math

from qsum.data.to_bytes import bytes_from_repr


def int_to_bytes(obj: int) -> bytes:
    """Convert int's in to the most compact byte representation possible

    CURRENTLY UNUSED, while cleverly packing integers tightly it's actually ~5x slower then just calling repr

    Args:
        obj: integer to convert to bytes

    Returns:
        bytes representing integer
    """
    return obj.to_bytes(1 if obj == 0 else math.floor((math.log2(abs(obj)) + 1) / 8 + 1), byteorder='big', signed=True)


def complex_to_bytes(obj) -> bytes:
    """
    Custom logic for converting complex numbers to bytes which handles the oddities around -0.0 and 0.0

    Args:
        obj: complex object to convert to bytes

    Returns:
        bytes representing the object
    """

    real, imag = obj.real, obj.imag
    # this line might seem odd, but think about -0.0 (which equals 0.0),
    new_complex = complex(0.0 if real == 0.0 else real, 0.0 if imag == 0.0 else imag)

    return bytes_from_repr(new_complex)
