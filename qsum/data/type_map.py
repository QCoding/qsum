from qsum.data.to_binary import str_to_binary
from qsum.data.wrappers import encode_wrapper

# maps a type to the function used to generate the binary data that will be hashed in to a checksum
TYPE_TO_BINARY_FUNCTION = {
    int: encode_wrapper(repr),
    str: str_to_binary,
}
