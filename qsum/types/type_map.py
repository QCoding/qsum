"""
For any given type we would like a fixed prefix value to guarantee types match when comparing checksums

We reserve 2 bytes (65536 unique values) for the compact representation of the type tyhat can be looked up against this
table, please observe the following reserved groups:

\x00: python builtin types
"""
#
PREFIX_BYTES = 2

TYPE_TO_PREFIX = {
    int: b'\x00\x00',
    str: b'\x00\x01',
    bool: b'\x00\x02',
    bytes: b'\x00\x03',
    float: b'\x00\x04',
    complex: b'\x00\x05',
    bytearray: b'\x00\x06',
}
PREFIX_TO_TYPE = {v: k for k, v in TYPE_TO_PREFIX.items()}
