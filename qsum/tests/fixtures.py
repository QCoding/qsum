import pytest


@pytest.fixture(scope='session')
def range_2_16():
    return range(-2 ** 16, 2 ** 16)
