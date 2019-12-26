from qsum import checksum
from qsum.core.dependency import resolve_dependencies


def test_resolve_dependencies_collection_type_independent():
    """Ensure resolve_depedencies produces consistent results for different collection types of the same packages"""
    assert resolve_dependencies(('pytest', 'setuptools')) == resolve_dependencies(
        ['pytest', 'setuptools']) == resolve_dependencies({'pytest', 'setuptools'})


def test_checksum_changes_with_dependency():
    """Validate that the checksum actually changes when we add a dep"""
    assert checksum(123, depends_on=('pytest',)) != checksum(123)
