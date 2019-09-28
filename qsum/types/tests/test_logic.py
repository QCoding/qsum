# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
import pytest

from qsum import checksum
from qsum.core.exceptions import QSumInvalidTypeException, QSumInvalidPrefixException
from qsum.types.logic import prefix_to_type
from qsum.types.type_map import RESERVED_INVALID_PREFIX


class Custom:
    def __init__(self):
        pass


@pytest.mark.xfail(raises=QSumInvalidTypeException, strict=True)
def test_invalid_type():
    _ = checksum(Custom())


@pytest.mark.xfail(raises=QSumInvalidPrefixException)
def test_prefix_to_type():
    prefix_to_type(RESERVED_INVALID_PREFIX)
