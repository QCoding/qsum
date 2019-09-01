from qsum import checksum
from qsum.types.logic import checksum_to_type
from qsum.tests.constants import BYTES_IN_CHECKSUM

# noinspection PyUnresolvedReferences
from qsum.tests.fixtures import *


def test_basic_str_abcd():
    c = checksum("abcd")
    assert c == b'\x00\x01\x88\xd4&o\xd4\xe63\x8d\x13\xb8E\xfc\xf2\x89W\x9d \x9c\x89x#\xb9!}\xa3\xe1a\x93o\x03\x15\x89', "Validate a specific checksum"


def test_bytes_in_checksum():
    c = checksum("adsfsdfdgerrgdgdggddg")
    assert len(c) == BYTES_IN_CHECKSUM, "Validate the number of bytes of the checksum"


def test_str_type():
    c = checksum("A nice string")
    assert checksum_to_type(c) == str


def test_str_uniqueness(range_2_16):
    str_values = map(str, range_2_16)
    value_checksums = set(map(checksum, str_values))
    assert len(value_checksums) == len(range_2_16)
