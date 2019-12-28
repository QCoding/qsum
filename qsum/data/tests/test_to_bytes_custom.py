# pylint: disable=wildcard-import,unused-wildcard-import,redefined-outer-name
from qsum.data import to_bytes_custom
from qsum.data.to_bytes_custom import int_to_bytes
from qsum.tests import helpers
# noinspection PyUnresolvedReferences
from qsum.tests.helpers import *


def test_integer_conversion_to_bytes(range_2_16):
    """Verify integers get unique byte strings"""
    all_byte_values = list(map(int_to_bytes, range_2_16))
    assert len(all_byte_values) == len(set(all_byte_values)), "Every integer should have a unique byte value"


def test_module_to_bytes_different_modules():
    """Verify two different modules result in two different checksums"""
    assert checksum(helpers) != checksum(to_bytes_custom)


def test_blank_checksum_file(tmp_path):
    """Blank files should have predicable checksums"""
    # write a blank file
    blank_file_path = tmp_path / 'blank_file.txt'
    with open(blank_file_path, 'w'):
        pass

    # text read mode
    text_file = open(blank_file_path, mode='r')
    assert Checksum(text_file).hex() == '00f0e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

    # binary read mode
    binary_file = open(blank_file_path, mode='rb')
    assert Checksum(binary_file).hex() == '00f1e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'


def test_checksum_file_changes(tmp_path):
    """Changing a file should change it's checksum"""
    # write a file
    file_path = tmp_path / 'file_to_checksum.txt'
    file_path.write_text("A great file\nIs only as good as")
    # text read mode
    text_file = open(file_path, mode='r')
    text_file_org_checksum = checksum(text_file)

    # binary read mode
    binary_file = open(file_path, mode='rb')
    binary_file_org_checksum = checksum(binary_file)

    # change the file
    file_path.write_text("It's weakeast line")

    # ensure the checksum changes when the file changes
    assert checksum(text_file) != text_file_org_checksum
    assert checksum(binary_file) != binary_file_org_checksum

    # ensure we seek back to the starting position
    assert text_file.tell() == 0
    assert binary_file.tell() == 0
