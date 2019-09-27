from qsum.core.logic import is_supported_type


class NotCheckSummable():
    pass


def test_is_supported_type():
    assert is_supported_type(str)
    assert not is_supported_type(NotCheckSummable)
