# pylint: disable=missing-function-docstring
# pylint: disable=unidiomatic-typecheck
"""
Generalized parametrized tests that should be added for every support type
"""
from collections import deque

import pytest

from qsum import checksum, Checksum
from qsum.core.constants import DEFAULT_BYTES_IN_CHECKSUM

TYPE_TO_VALUE_EXAMPLES = (
    (str, "adsfsdfdgerrgdgdggddg"),
    (int, -353535),
    (bool, True),
    (bytes, b"\x0a02\x043b\x1721"),
    (float, 3535.2524),
    (complex, complex('145.2424-1.5j')),
    (bytearray, bytearray(10)),
    (tuple, ('a', 'b', 'c', 'd', 'e')),
    (list, [0.1, 0.2, 0.3]),
    (deque, deque(['item_1', 'item_2', 'item_3'])),
    (dict, {'a': 1, 'b': 2}),
    (type, str),
)

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
    (complex('-5.1+17.0j'), '0005bd889c362cd9496951986d4901bc8301d725026178da790719b3809a7282700e'),

    # tuple
    ((1, 2, 3), '010020b387396ae6fae6804de8566844ab008e5597825326ee53181515dbf5538570'),

    # list
    (['a', 'b', 'c'], '0101525f861900d34d6361808f22790f48bee9b28f7a09ac41ba7a545595ce795fff'),

    # deque
    (deque([complex('-5.1+17.0j'), 21442, 12.1]),
     '0102be57788e518c3307f05cdf6959480b5268f37977e300465b799aadd82f246cfa'),

    # dict
    ({'a': [1, 2, 3], 'b': (1, 2, 3), 'c': deque([1, 2, 3])},
     '01033e95026bed200c7b2794a5a55a0cbde7a73faa1c3722e1fcc947a767c2e8660e'),

    # type (note we're just using int as an example type here)
    (int, '0007f918a1a5caa5f9fe881535f5846de4549fb2809063c3fc932c258d864fc0c17c'),
)


@pytest.mark.parametrize('value', [x for _, x in TYPE_TO_VALUE_EXAMPLES])
def test_bytes_in_checksum(value):
    assert len(checksum(value)) == DEFAULT_BYTES_IN_CHECKSUM, "Validate the number of bytes of the checksum"


@pytest.mark.parametrize('obj_type,value', TYPE_TO_VALUE_EXAMPLES)
def test_expected_type(obj_type, value):
    assert type(value) == Checksum.checksum(value).type == obj_type


@pytest.mark.parametrize('value,expected_checksum', VALUE_TO_CHECKSUM_EXAMPLES)
def test_expected_checksum(value, expected_checksum):
    checksum_bytes = Checksum.checksum(value).hex()
    assert checksum_bytes == expected_checksum, "Got '{}'\nExpected '{}' for the checksum of '{}'".format(
        checksum_bytes, expected_checksum, value)


@pytest.mark.parametrize('values', [[True, False]])
def test_unique_checksums_by_type(values):
    value_checksums = set(map(checksum, values))
    assert len(value_checksums) == len(values)
