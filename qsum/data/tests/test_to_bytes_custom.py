# pylint: disable=wildcard-import,unused-wildcard-import,redefined-outer-name
from qsum.data.to_bytes_custom import int_to_bytes
# noinspection PyUnresolvedReferences
from qsum.tests.helpers import *


def test_integer_conversion_to_bytes(range_2_16):
    """Verify integers get unique byte strings"""
    all_byte_values = list(map(int_to_bytes, range_2_16))
    assert len(all_byte_values) == len(set(all_byte_values)), "Every integer should have a unique byte value"
