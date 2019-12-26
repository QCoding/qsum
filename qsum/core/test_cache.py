import pkg_resources
import pytest

from qsum.core.cache import get_package_version


@pytest.mark.xfail(raises=pkg_resources.DistributionNotFound, strict=True)
def test_get_package_version_bad_package():
    get_package_version('foo')


def test_get_package_version():
    assert tuple(map(int, get_package_version('pytest').split('.'))) > (4, 4, 0)
