"""
Generalized parametrized tests that should be added for every support type
"""

import pytest

from qsum import checksum
from qsum.core.constants import BYTES_IN_CHECKSUM


@pytest.mark.parametrize('value', ["adsfsdfdgerrgdgdggddg", -353535, True])
def test_bytes_in_checksum(value):
    assert len(checksum(value)) == BYTES_IN_CHECKSUM, "Validate the number of bytes of the checksum"


@pytest.mark.parametrize('values', [[True, False]])
def test_unique_checksums_by_type(values):
    value_checksums = set(map(checksum, values))
    assert len(value_checksums) == len(values)


@pytest.mark.parametrize('value,expected_checksum', [
    (True, b"\x00\x02\xc5\xb7\xcdU\x00\x93\xd9\xbdT^D\x01\xc2\xc9\xa2\xe81\x11O\x9e;\x9e\xff\r;\xdeS|\xc4\x99\xc8v"),
    (0, b"\x00\x00_\xec\xebf\xff\xc8o8\xd9Rxlmily\xc2\xdb\xc29\xddN\x91\xb4g)\xd7:'\xfbW\xe9"),
    ("abcd", b"\x00\x01\x88\xd4&o\xd4\xe63\x8d\x13\xb8E\xfc\xf2\x89W\x9d \x9c\x89x#\xb9!}\xa3\xe1a\x93o\x03\x15\x89")
])
def test_expected_checksum(value, expected_checksum):
    assert checksum(value) == expected_checksum
