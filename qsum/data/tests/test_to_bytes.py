from qsum.data.to_bytes import bytes_from_repr_with_overrides


def test_bytes_from_repr_with_overrides_value():
    override = "Foo_Override"
    assert bytes_from_repr_with_overrides("Foo", value_overrides={'Foo': override}).decode() == "'" + override + "'"
