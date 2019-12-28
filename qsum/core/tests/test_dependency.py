from qsum import checksum, Checksum
from qsum.core.constants import DependsOn, DEFAULT_BYTES_IN_CHECKSUM
from qsum.core.dependency import resolve_dependencies


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


def test_python_env_dependency():
    """Simple test of DependsOn.PythonEnv"""
    assert len(checksum('abc', depends_on=(DependsOn.PythonEnv,))) == DEFAULT_BYTES_IN_CHECKSUM
