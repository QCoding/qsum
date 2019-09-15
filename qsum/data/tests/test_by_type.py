"""
Generalized parametrized tests that should be added for every support type
"""

import pytest

from qsum import checksum
from qsum.core.constants import BYTES_IN_CHECKSUM

TYPE_TO_VALUE_EXAMPLES = {
    str: "adsfsdfdgerrgdgdggddg",
    int: -353535,
    bool: True,
    bytes: b"\x0a02\x043b\x1721",
    float: 3535.2524,
}

# DO NOT USE A DICT HERE, we don't want to rely on cross type equality
# TODO: use hex strings
VALUE_TO_CHECKSUM_EXAMPLES = (
        # Bool
        (True, b"\x00\x02\xc5\xb7\xcdU\x00\x93\xd9\xbdT^D\x01\xc2\xc9\xa2\xe81\x11O\x9e;\x9e\xff\r;\xdeS|\xc4\x99\xc8v"),

        # Int
        (0, b"\x00\x00_\xec\xebf\xff\xc8o8\xd9Rxlmily\xc2\xdb\xc29\xddN\x91\xb4g)\xd7:'\xfbW\xe9"),

        # Str
        ("abcd",
         b"\x00\x01\x88\xd4&o\xd4\xe63\x8d\x13\xb8E\xfc\xf2\x89W\x9d \x9c\x89x#\xb9!}\xa3\xe1a\x93o\x03\x15\x89"),

        # Bytes
        (b"\x0f01\x04ab\x1721",
         b'\x00\x03\xb7\xf7\x0c\xe1\xc2\xd5\xf5N\x8c\x0f\x07F\xcc:>\xe9\xeayE\n1\x94%\xdb\xfd \xff\xc1:\xab8\x0c'),

        # Float
        (31134.234, b'\x00\x04\x86\xa1\xd4\x95*\xfb\xd6\xd7@X5\x83?2[\x99^0\xaf\xa4\xbe{\xfb\xa1\x0c\x96le\xa7S-v'),
        (0.0, b"\x00\x04\x8a\xedd+\xf5\x11\x8b\x9d<\x85\x9b\xd4\xbe5\xec\xacu\xb6\xe8s\xcc\xe3N{oUK\x06\xf7UP\xd7"),
        (-0.0, b"\x00\x04\x8a\xedd+\xf5\x11\x8b\x9d<\x85\x9b\xd4\xbe5\xec\xacu\xb6\xe8s\xcc\xe3N{oUK\x06\xf7UP\xd7")
)


@pytest.mark.parametrize('value', TYPE_TO_VALUE_EXAMPLES.values())
def test_bytes_in_checksum(value):
    assert len(checksum(value)) == BYTES_IN_CHECKSUM, "Validate the number of bytes of the checksum"


@pytest.mark.parametrize('value,expected_checksum', VALUE_TO_CHECKSUM_EXAMPLES)
def test_expected_checksum(value, expected_checksum):
    c = checksum(value)
    assert c == expected_checksum, "Got {}\nExpected {}".format(c, expected_checksum)


@pytest.mark.parametrize('values', [[True, False]])
def test_unique_checksums_by_type(values):
    value_checksums = set(map(checksum, values))
    assert len(value_checksums) == len(values)
