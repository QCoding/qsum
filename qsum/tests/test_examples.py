# pylint: disable=missing-function-docstring,missing-module-docstring
from qsum.examples import basic_checksum
from qsum.examples import checksum_performance
from qsum.examples import combine_checksums
from qsum.examples import cprofile_long_list
from qsum.examples import inherited_container
from qsum.examples import misc_checksums
from qsum.examples import package_versions
from qsum.examples import using_checksums


def test_basic_checksum():
    basic_checksum.main()


def test_checksum_performance():
    checksum_performance.main()


def test_combine_checksums():
    combine_checksums.main()


def test_cprofile_long_list():
    cprofile_long_list.main()


def test_inherited_container():
    inherited_container.main()


def test_misc_checksums():
    misc_checksums.main()


def test_package_versions():
    package_versions.main()


def test_using_checksums():
    using_checksums.main()
