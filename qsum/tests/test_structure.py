from qsum.data.logic import all_data_types
from qsum.types.logic import all_prefix_types


def test_prefix_and_data_support():
    "Validate prefix type logic and data support the same set of types"
    assert set(all_data_types()) == set(all_prefix_types())
