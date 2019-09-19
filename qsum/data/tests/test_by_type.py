"""
Generalized parametrized tests that should be added for every support type
"""

import pytest

from qsum import checksum, Checksum
from qsum.core.constants import BYTES_IN_CHECKSUM

TYPE_TO_VALUE_EXAMPLES = {
    str: "adsfsdfdgerrgdgdggddg",
    int: -353535,
    bool: True,
    bytes: b"\x0a02\x043b\x1721",
    float: 3535.2524,
    complex: complex('145.2424-1.5j'),
    bytearray: bytearray(10),
}

VALUE_TO_CHECKSUM_EXAMPLES = (
    # bool
    (True, '00023cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18'),
    (False, '000260a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe'),

    # int
    (0, '00005feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'),

    # str
    ("abcd", '000188d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589'),

    # bytes
    (b"\x0f01\x04ab\x1721", '0003b7f70ce1c2d5f54e8c0f0746cc3a3ee9ea79450a319425dbfd20ffc13aab380c'),

    # bytearray
    (bytearray(range(10)), '00061f825aa2f0020ef7cf91dfa30da4668d791c5d4824fc8e41354b89ec05795ab3'),

     # float
     (31134.234, '000486a1d4952afbd6d7405835833f325b995e30afa4be7bfba10c966c65a7532d76'),
     (0.0, '00048aed642bf5118b9d3c859bd4be35ecac75b6e873cce34e7b6f554b06f75550d7'),
     (-0.0, '00048aed642bf5118b9d3c859bd4be35ecac75b6e873cce34e7b6f554b06f75550d7'),

     # complex
     (complex('-5.1+17.0j'), '0005bd889c362cd9496951986d4901bc8301d725026178da790719b3809a7282700e')
     )

@pytest.mark.parametrize('value', TYPE_TO_VALUE_EXAMPLES.values())
def test_bytes_in_checksum(value):
    assert len(checksum(value)) == BYTES_IN_CHECKSUM, "Validate the number of bytes of the checksum"


@pytest.mark.parametrize('value,expected_checksum', VALUE_TO_CHECKSUM_EXAMPLES)
def test_expected_checksum(value, expected_checksum):
    c = Checksum.checksum(value).hex()
    assert c == expected_checksum, "Got '{}'\nExpected '{}' for the checksum of '{}'".format(c, expected_checksum,
                                                                                             value)


@pytest.mark.parametrize('values', [[True, False]])
def test_unique_checksums_by_type(values):
    value_checksums = set(map(checksum, values))
    assert len(value_checksums) == len(values)
