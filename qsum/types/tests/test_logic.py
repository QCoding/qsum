import pytest

from qsum import checksum
from qsum.core.exceptions import QSumInvalidDataTypeException, QSumInvalidTypeException


class Custom:
    def __init__(self):
        pass


@pytest.mark.xfail(raises=QSumInvalidTypeException, strict=True)
def test_invalid_type():
    c = checksum(Custom())
