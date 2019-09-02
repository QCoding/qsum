"""
Generalized parametrized tests that should be added for every support type
"""

import pytest

from qsum import checksum
from qsum.core.constants import BYTES_IN_CHECKSUM


@pytest.mark.parametrize('value', [
    # Str
    "adsfsdfdgerrgdgdggddg",
    # Int
    -353535,
    # Bool
    True,
    # Bytes
    b"\x0a02\x043b\x1721"])
def test_bytes_in_checksum(value):
    assert len(checksum(value)) == BYTES_IN_CHECKSUM, "Validate the number of bytes of the checksum"


@pytest.mark.parametrize('values', [[True, False]])
def test_unique_checksums_by_type(values):
    value_checksums = set(map(checksum, values))
    assert len(value_checksums) == len(values)


@pytest.mark.parametrize('value,expected_checksum', [
    # Bool
    (True, b"\x00\x02\xc5\xb7\xcdU\x00\x93\xd9\xbdT^D\x01\xc2\xc9\xa2\xe81\x11O\x9e;\x9e\xff\r;\xdeS|\xc4\x99\xc8v"),
    # Int
    (0, b"\x00\x00_\xec\xebf\xff\xc8o8\xd9Rxlmily\xc2\xdb\xc29\xddN\x91\xb4g)\xd7:'\xfbW\xe9"),
    # Str
    ("abcd", b"\x00\x01\x88\xd4&o\xd4\xe63\x8d\x13\xb8E\xfc\xf2\x89W\x9d \x9c\x89x#\xb9!}\xa3\xe1a\x93o\x03\x15\x89"),
    # Bytes
    (b"\x0f01\x04ab\x1721", b'\x00\x03\xb7\xf7\x0c\xe1\xc2\xd5\xf5N\x8c\x0f\x07F\xcc:>\xe9\xeayE\n1\x94%\xdb\xfd \xff\xc1:\xab8\x0c')
])
def test_expected_checksum(value, expected_checksum):
    c = checksum(value)
    assert c == expected_checksum, "Got {}\nExpected {}".format(c, expected_checksum)
