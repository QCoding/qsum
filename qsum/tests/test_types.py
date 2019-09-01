import pytest

from qsum import checksum
from qsum.core.types import QSumInvalidTypeException
from qsum.data.logic import QSumInvalidDataTypeException


class Custom:
    def __init__(self):
        pass


@pytest.mark.xfail(raises=QSumInvalidTypeException, strict=True)
def test_invalid_type():
    c = checksum(Custom())
