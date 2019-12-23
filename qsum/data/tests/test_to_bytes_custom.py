# pylint: disable=wildcard-import,unused-wildcard-import,redefined-outer-name
from qsum.data import to_bytes_custom
from qsum.data.to_bytes_custom import int_to_bytes
from qsum.tests import helpers
# noinspection PyUnresolvedReferences
from qsum.tests.helpers import *


def test_integer_conversion_to_bytes(range_2_16):
    """Verify integers get unique byte strings"""
    all_byte_values = list(map(int_to_bytes, range_2_16))
    assert len(all_byte_values) == len(set(all_byte_values)), "Every integer should have a unique byte value"


def test_module_to_bytes_different_modules():
    assert checksum(helpers) != checksum(to_bytes_custom)
