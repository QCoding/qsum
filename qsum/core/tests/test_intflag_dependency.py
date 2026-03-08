import pytest
from qsum import checksum
from qsum.core.constants import DependsOn, DEFAULT_BYTES_IN_CHECKSUM

def test_depends_on_intflag_combination():
    """Verify that combining DependsOn flags works and produces the same result as a tuple"""
    # Create a checksum with combined flags
    checksum_combined = checksum('abc', depends_on=DependsOn.PythonEnv | DependsOn.Platform)

    # Create a checksum with a tuple of flags
    # Note: the order in the tuple shouldn't matter for the final checksum if resolve_dependencies handles it right,
    # but currently resolve_dependencies returns a dict.
    # The checksum logic sorts dictionary items before checksumming.
    checksum_tuple = checksum('abc', depends_on=(DependsOn.PythonEnv, DependsOn.Platform))

    assert checksum_combined == checksum_tuple
    assert len(checksum_combined) == DEFAULT_BYTES_IN_CHECKSUM

def test_depends_on_intflag_single():
    """Verify single flag still works"""
    checksum_single = checksum('abc', depends_on=DependsOn.PythonEnv)
    assert len(checksum_single) == DEFAULT_BYTES_IN_CHECKSUM

def test_depends_on_intflag_mixed_with_tuple():
    """Verify that we can mix IntFlag logic if needed, though type hint says collection OR DependsOn"""
    # resolve_dependencies expects DependsOnType which is Union[tuple, ..., DependsOn]
    # If we pass a tuple containing DependsOn flags, it should work as before.
    checksum_tuple = checksum('abc', depends_on=(DependsOn.PythonEnv, DependsOn.Platform))
    assert len(checksum_tuple) == DEFAULT_BYTES_IN_CHECKSUM

def test_intflag_values():
    """Verify the values are integers"""
    assert DependsOn.PythonEnv.value == 1
    assert DependsOn.PythonVer.value == 2
    assert DependsOn.Platform.value == 4
    assert DependsOn.QSumVer.value == 8
