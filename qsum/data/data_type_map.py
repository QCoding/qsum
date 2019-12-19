import functools
import types
import typing

from qsum.core.constants import ChecksumCollection
from qsum.core.exceptions import QSumInvalidDataTypeException
from qsum.data.to_bytes import str_to_bytes, bytes_from_repr, bytes_to_bytes, bytes_from_repr_with_overrides, \
    singleton_to_bytes
from qsum.data.to_bytes_custom import complex_to_bytes, function_to_bytes


def raise_type_exception(_, data_type) -> None:
    """Raise an exception for the given type

    Args:
        _: accepts the object to conform to the required signature
        data_type: the specific type to raise an exception for

    Raises:
        QSumInvalidDataTypeException
    """
    raise QSumInvalidDataTypeException(
        "{} is registered as an invalid type for computing a data checksum".format(data_type))


# since we use this one in the data checksum implementation and want to avoid looking it up every time
TYPE_CLASS_TO_BYTES_FUNCTION = bytes_from_repr

# maps a type to the function used to generate the bytes data that will be hashed in to a checksum
TYPE_TO_BYTES_FUNCTION = {
    # simply get the bytes from the repr of the object
    int: bytes_from_repr,
    bool: bytes_from_repr,
    type: TYPE_CLASS_TO_BYTES_FUNCTION,
    range: bytes_from_repr,
    type(None): singleton_to_bytes,
    type(Ellipsis): singleton_to_bytes,

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

    # very custom logic
    types.FunctionType: function_to_bytes,

    # registered as invalid data types to checksum
    ChecksumCollection: functools.partial(raise_type_exception, data_type=ChecksumCollection),
}  # type: typing.Dict[typing.Type, typing.Callable]
