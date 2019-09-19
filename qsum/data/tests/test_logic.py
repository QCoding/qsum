import pytest

from qsum.core.exceptions import QSumInvalidDataTypeException
from qsum.data import data_checksum


class Custom:
    def __init__(self):
        pass


@pytest.mark.xfail(raises=QSumInvalidDataTypeException, strict=True)
def test_invalid_type():
    custom = Custom()
    c = data_checksum(custom, type(custom))
