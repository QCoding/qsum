from qsum.data.to_bytes import str_to_bytes, repr_to_bytes

# maps a type to the function used to generate the bytes data that will be hashed in to a checksum
from qsum.data.to_static import bool_to_static

TYPE_TO_BYTES_FUNCTION = {
    int: repr_to_bytes,
    str: str_to_bytes,
    bool: bool_to_static,
}
