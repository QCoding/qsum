"""
For any given type we would like a fixed prefix value to guarantee types match when comparing checksums

We reserve 2 bytes (65536 unique values) for the compact representation of the type tyhat can be looked up against this
table, please observe the following reserved groups:
    \x00: builtin python types that represent individual objects
    \x01: builtin python containers and collections
    \xff: special types used by qsum
"""
import types
from collections import deque
from io import TextIOWrapper, BufferedReader, BufferedWriter

from qsum.core.constants import ChecksumCollection, DependsOn

PREFIX_BYTES = 2

# *** special prefixes ***
CHECKSUM_TYPE_PREFIX = b'\xff\x00'  # Checksum class
UNREGISTERED_TYPE_PREFIX = b'\xff\xaa'  # An unregistered type
RESERVED_INVALID_PREFIX = b'\xff\xff'  # Invalid prefix for testing

# mostly for validating uniqueness
SPECIAL_PREFIXES = {CHECKSUM_TYPE_PREFIX, UNREGISTERED_TYPE_PREFIX, RESERVED_INVALID_PREFIX}

# *************************

TYPE_TO_PREFIX = {
    # \x00: builtin python types that represent individual objects
    int: b'\x00\x00',
    str: b'\x00\x01',
    bool: b'\x00\x02',
    bytes: b'\x00\x03',
    float: b'\x00\x04',
    complex: b'\x00\x05',
    bytearray: b'\x00\x06',
    type: b'\x00\x07',
    range: b'\x00\x08',
    memoryview: b'\x00\x09',
    # https://stackoverflow.com/questions/15844714/why-am-i-getting-an-error-message-in-python-cannot-import-name-nonetype
    type(None): b'\x00\x0a',
    type(Ellipsis): b'\x00\x0b',

    # types from open built-in function
    TextIOWrapper: b'\x00\xf0',
    BufferedReader: b'\x00\xf1',

    # types requiring use of types module for definition
    types.ModuleType: b'\x00\xcc',  # module is special, let's get it a code name \xcc
    types.FunctionType: b'\x00\xff',  # function is pretty special, let it have the \xff name

    # \x01: builtin python containers and collections that require custom logic to handle breaking open contents
    tuple: b'\x01\x00',
    list: b'\x01\x01',
    deque: b'\x01\x02',
    dict: b'\x01\x03',
    set: b'\x01\x04',
    frozenset: b'\x01\x05',

    # \xff: special types used by qsum
    ChecksumCollection: b'\xff\x11',
    DependsOn: b'\xff\xc0',
}
PREFIX_TO_TYPE = {v: k for k, v in TYPE_TO_PREFIX.items()}
