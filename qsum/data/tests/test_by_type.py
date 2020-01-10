# pylint: disable=missing-function-docstring,unidiomatic-typecheck
"""
Generalized parametrized tests that should be added for every support type
"""
import types
from collections import deque
from datetime import date, datetime

import pytest

from qsum import checksum, Checksum
from qsum.core.constants import DEFAULT_BYTES_IN_CHECKSUM, DependsOn
from qsum.tests import helpers
from qsum.tests.helpers import foo_function

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
    (range, range(0)),
    (memoryview, memoryview(b'abc')),
    (set, set([1, 2, 3])),
    (frozenset, frozenset([3, 4.3, 5])),
    (type(None), None),
    (type(Ellipsis), Ellipsis),
    (types.FunctionType, foo_function),
    (types.ModuleType, helpers),
    (DependsOn, DependsOn.PythonEnv),
    (date, date(1964, 1, 15)),
    (datetime, datetime(1980, 1, 5, 1, 2, 3)),

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
     '010329703d1740514032aee0de4de342933fb231822ca62edb413d31f77bf1e32e32'),

    # type (note we're just using int as an example type here)
    (int, '0007f918a1a5caa5f9fe881535f5846de4549fb2809063c3fc932c258d864fc0c17c'),

    # range
    (range(0, 10, 3), '0008547cc0cc2d8a96bf35d2bee0a2df9cbf9bc7ffae2b87e95cf87d1903b914cf0d'),

    # memoryview
    (memoryview(b'def'), '0009cb8379ac2098aa165029e3938a51da0bcecfc008fd6795f401178647f96c5b34'),

    # set
    ({1, 1.1, complex('1.2')}, '0104b96e73b739fbcf74e0f2d385df2ed8003b0eaaa4a9404e7ed0e8361641fb4bfd'),

    # frozenset
    (frozenset(['a', b'\xff', False]), '01052051878e48ce6d4925bd329fb4e6cb3147fc0f06edd5dc32a020f04a10193797'),

    # None
    (None, '000a6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d'),

    # Ellipsis
    (Ellipsis, '000b6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d'),

    # Function
    (foo_function, '00ff57155365be65f118fcc96e2d3ee556aaf62e72baa2a16bd8b36da39120987743'),

    # Module (whenever you add to helpers this checksum has to be adjusted)
    (helpers, '00ccf0aed8a77e814394a6f6194a4f8052fb33cfa6ad8bb6572f8f5caf28f693083f'),

    # DependsOn
    (DependsOn.PythonEnv, 'ffc01b5376344d56a72494651932ca29d63df34921e01e98b296210f21848337a796'),

    # Date
    (date(2012, 1, 1), '10dd5bb050078f9028efcf5ce1e6c8107c582bdc3607346ab17fc9e8622b586acd6e'),

    # DateTime
    (datetime(2012, 1, 1, 4, 30, 20), '10d01f2db0e7b1951bba86ead2fe47722dad899f54c81cc3a4c16db7357c8e787769'),
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
