import functools

from qsum.data.to_bytes import str_to_bytes, bytes_from_repr, bytes_to_bytes, bytes_from_repr_with_overrides
from qsum.data.to_bytes_custom import complex_to_bytes

# maps a type to the function used to generate the bytes data that will be hashed in to a checksum
TYPE_TO_BYTES_FUNCTION = {
    # simply get the bytes from the repr of the object
    int: bytes_from_repr,
    bool: bytes_from_repr,
    type: bytes_from_repr,
    range: bytes_from_repr,

    # string can be encoded in to bytes
    str: str_to_bytes,

    # bytes are bytes
    bytes: bytes_to_bytes,
    bytearray: bytes_to_bytes,

    # some types already implement __bytes__
    memoryview: bytes,

    # some custom logic required
    float: functools.partial(bytes_from_repr_with_overrides, repr_overrides={'-0.0': '0.0'}),
    complex: complex_to_bytes,
}
