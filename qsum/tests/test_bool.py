from qsum import checksum
from qsum.tests.constants import BYTES_IN_CHECKSUM
from qsum.types.logic import checksum_to_type


def test_checksum_true():
    c = checksum(True)
    assert c == b"\x00\x02\xc5\xb7\xcdU\x00\x93\xd9\xbdT^D\x01\xc2\xc9\xa2\xe81\x11O\x9e;\x9e\xff\r;\xdeS|\xc4\x99\xc8v", "Validate a specific checksum"


def test_bools_generate_unique_checksums():
    bool_values = [True, False]
    value_checksums = set(map(checksum, bool_values))
    assert len(value_checksums) == len(bool_values)


def test_bool_type():
    c = checksum(False)
    assert checksum_to_type(c) == bool


def test_bytes_in_checksum():
    c = checksum(True)
    assert len(c) == BYTES_IN_CHECKSUM
