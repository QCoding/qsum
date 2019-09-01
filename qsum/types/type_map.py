PREFIX_BYTES = 2
TYPE_TO_PREFIX = {
    int: b'\x00\x00',
    str: b'\x00\x01',
}
PREFIX_TO_TYPE = {v: k for k, v in TYPE_TO_PREFIX.items()}