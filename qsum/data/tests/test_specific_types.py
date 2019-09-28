# pylint: disable=redefined-outer-name
# pylint: disable=missing-function-docstring
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

"""Some type specific tests that are hard to do in test_by_type"""

from qsum.core.logic import checksum, Checksum

# noinspection PyUnresolvedReferences
from qsum.tests.fixtures import *


def test_integers_generate_unique_checksums(range_2_16):
    value_checksums = set(map(checksum, range_2_16))
    assert len(value_checksums) == len(range_2_16)


def test_str_uniqueness(range_2_16):
    str_values = map(str, range_2_16)
    value_checksums = set(map(checksum, str_values))
    assert len(value_checksums) == len(range_2_16)


def test_float_uniqueness(range_2_16):
    float_values = map(float, range_2_16)
    value_checksums = set(map(checksum, float_values))
    assert len(value_checksums) == len(range_2_16)


def test_complex_uniqueness(range_2_16):
    complex_values = [complex(re, im) for re, im in zip(range_2_16, reversed(range_2_16))]
    complex_checksums = set(map(checksum, complex_values))
    assert len(complex_checksums) == len(range_2_16)


def test_float_0_0_equality():
    assert checksum(0.0) == checksum(-0.0)
    assert checksum(-0.0) == checksum(0.0)


def test_tuple_changes():
    assert checksum((0, 1, 2)) != checksum((-1, 1, 2))
    assert checksum((0, 1, 2)) != checksum((2, 1, 0))


def test_list_changes():
    example_list = [1, 2, 3]
    c_1 = checksum(example_list)
    example_list.append(4)
    c_2 = checksum(example_list)
    assert c_1 != c_2


def test_nested_dict():
    my_dict = {'a': {'b': {'c': 1}}}
    assert Checksum.checksum(my_dict).type == dict
