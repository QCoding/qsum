import pytest

from qsum import checksum, Checksum, qsum_version
from qsum.core.constants import DependsOn, DEFAULT_BYTES_IN_CHECKSUM, UNKNOWN_VERSION
from qsum.core.dependency import resolve_dependencies, resolve_dependency
from qsum.core.exceptions import QSumInvalidDependsOn, QSumUnknownVersionDependency


def test_resolve_dependencies_collection_type_independent():
    """Ensure resolve_depedencies produces consistent results for different collection types of the same packages"""
    assert resolve_dependencies(('pytest', 'setuptools')) == resolve_dependencies(
        ['pytest', 'setuptools']) == resolve_dependencies({'pytest', 'setuptools'})


def test_checksum_changes_with_dependency():
    """Validate that the checksum actually changes when we add a dep"""
    assert checksum(123, depends_on=('pytest',)) != checksum(123)


def test_dependency_original_type():
    """Ensure we get the original type right even if adding depends_on"""
    assert Checksum('abc', depends_on=('pytest',)).type == str


# Mock the version so the test will patch locally when developing code
@pytest.mark.parametrize('depends_on', [d for d in DependsOn if d != DependsOn.QSumVer])
def test_depends_on_values(depends_on):
    """Simple test of DependsOn.PythonEnv that also validates depends_on support of single DependsOn enum values"""
    assert len(checksum('abc', depends_on=depends_on)) == DEFAULT_BYTES_IN_CHECKSUM


@pytest.mark.xfail(condition=qsum_version() == UNKNOWN_VERSION, raises=QSumUnknownVersionDependency, astrict=True,
                   reason="when running in dev environment we expect this to fail, "
                          "but if the package is installed this test will pass")
def test_depends_on_qsum_version():
    """Special test for qsum_version dep since the version isn't always available"""
    assert len(checksum('abc', depends_on=DependsOn.QSumVer)) == DEFAULT_BYTES_IN_CHECKSUM


def test_invalid_dependency():
    """Make sure that a misc type passed to resolve_dependency fails"""
    with pytest.raises(QSumInvalidDependsOn):
        resolve_dependency(1)
