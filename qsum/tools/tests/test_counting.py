import pytest

from qsum import Checksum, checksum
from qsum.tools.counting import count_types
from qsum.core.exceptions import QSumInvalidChecksum


def test_count_types():
    checksums = list(map(checksum, [1, 2, 3, 'a', 'b', 'c', 'd', 5.5, 6.6]))
    counts = count_types(checksums)

    assert counts[int] == 3
    assert counts[str] == 4
    assert counts[float] == 2

def test_count_types_empty():
    counts = count_types([])
    assert len(counts) == 0

def test_count_types_single():
    counts = count_types([checksum(1)])
    assert counts[int] == 1
    assert len(counts) == 1

def test_count_types_multiple_same():
    counts = count_types(list(map(checksum, [1, 1, 1, 1])))
    assert counts[int] == 4
    assert len(counts) == 1

def test_count_types_complex_types():
    checksums = list(map(checksum, [[1, 2], {'a': 1}, (1, 2), set([1, 2])]))
    counts = count_types(checksums)

    assert counts[list] == 1
    assert counts[dict] == 1
    assert counts[tuple] == 1
    assert counts[set] == 1
    assert len(counts) == 4

def test_count_types_bytes():
    checksums = list(map(checksum, [1, 2, 'a']))
    counts = count_types(checksums)

    assert counts[int] == 2
    assert counts[str] == 1
    assert len(counts) == 2

def test_count_types_hex():
    checksums = list(map(lambda x: checksum(x).hex(), [1, 2, 'a']))
    counts = count_types(checksums)

    assert counts[int] == 2
    assert counts[str] == 1
    assert len(counts) == 2

def test_count_types_checksum_objects():
    checksums = list(map(Checksum, [1, 2, 'a']))
    counts = count_types(checksums)

    assert counts[int] == 2
    assert counts[str] == 1
    assert len(counts) == 2

def test_count_types_generator():
    checksums = map(checksum, [1, 2, 'a'])
    counts = count_types(checksums)

    assert counts[int] == 2
    assert counts[str] == 1
    assert len(counts) == 2

def test_count_types_invalid_checksum():
    with pytest.raises(QSumInvalidChecksum):
        count_types([1, 2, 3])
