# pylint: disable=missing-function-docstring,function-redefined
from qsum import checksum
from qsum.tests.helpers import foo_checksum


def test_function_attributes_change_checksum():
    def foo1():
        pass

    before_attribute, no_change = checksum(foo1), checksum(foo1)
    foo1.version = 1
    after_attribute = checksum(foo1)
    foo1.version += 1
    changing_attribute = checksum(foo1)

    assert before_attribute == no_change, "Function checksum unstable"
    assert before_attribute != after_attribute, "Adding attribute should change checksum"
    assert changing_attribute != after_attribute, "Changing attribute should change checksum"


def test_function_source_changes():
    def another_foo_function():
        return 1

    return_1 = checksum(another_foo_function)

    def another_foo_function():
        return 2

    return_2 = checksum(another_foo_function)

    assert return_1 != return_2


def test_function_same_module_same_source_stable():
    def another_foo_function():
        pass

    original = checksum(another_foo_function)

    def another_foo_function():
        pass

    redefined = checksum(another_foo_function)

    assert original == redefined


def foo_function():
    pass


def local_foo_checksum():
    return checksum(foo_function)


def test_same_function_different_module_different_checksum():
    """Validate that the same function defined in two modules will checksum differently

    To make this test meaningful, the foo's had to be defined with the same level of indents otherwise
    the source code will cause them to be different, we want to verify that we are adding the module a function
    is defined in to it's checksum
    """
    assert foo_checksum() != local_foo_checksum()
