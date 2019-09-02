PREFIX_BYTES = 2
TYPE_TO_PREFIX = {
    int: b'\x00\x00',
    str: b'\x00\x01',
    bool: b'\x00\x02',
    bytes: b'\x00\x03'
}
PREFIX_TO_TYPE = {v: k for k, v in TYPE_TO_PREFIX.items()}