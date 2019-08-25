TYPE_TO_PREFIX = {
    int: b'\x00\x00',
    str: b'\x00\x01',
}

PREFIX_TO_TYPE = {v: k for k, v in TYPE_TO_PREFIX.items()}

PREFIX_BYTES = 2


def type_to_prefix(obj_type):
    return TYPE_TO_PREFIX[obj_type]


def prefix_to_type(type_prefix):
    return PREFIX_TO_TYPE[type_prefix]


def checksum_to_type(checksum):
    """Extract the prefix bytes from the checksum and lookup the type"""
    return prefix_to_type(checksum[:PREFIX_BYTES])


def type_checksum(obj_type):
    # TODO: have an option to compress the type prefix
    return type_to_prefix(obj_type)
