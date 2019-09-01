from qsum.tests.constants import BYTES_IN_PREFIX
from qsum.types.type_map import TYPE_TO_PREFIX


def test_types_prefix_bytes():
    for v in TYPE_TO_PREFIX.values():
        assert len(v) == BYTES_IN_PREFIX
