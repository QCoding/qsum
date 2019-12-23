# pylint: disable=too-few-public-methods,missing-function-docstring
import pytest

from qsum import Checksum, checksum

STR_CHECKSUM_OBJS = [Checksum('123'),
                     '0001a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
                     bytes.fromhex('0001a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3')]
INT_CHECKSUM_OBJS = [Checksum(123), '0000a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
                     bytes.fromhex('0000a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3')]


@pytest.fixture(scope='session')
def range_2_16():
    """Create a range fixture for use in pytests"""
    return range(-2 ** 16, 2 ** 16)


class Custom:
    """A Custom class to try and checksum"""


class CustomDict1(dict):
    """A Custom Class that inherits from dict"""


class CustomDict2(dict):
    """Another Custom Class that inherits from dict"""


def foo_function():
    pass


def foo_checksum():
    return checksum(foo_function)
