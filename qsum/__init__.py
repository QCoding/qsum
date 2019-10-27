import pkg_resources

from qsum.core import exceptions
from qsum.core.logic import checksum, checksum_hex, Checksum, is_supported_type
from qsum.util._tester import test

try:
    __version__ = pkg_resources.get_distribution('qsum').version
except pkg_resources.DistributionNotFound:
    __version__ = "unknown"
