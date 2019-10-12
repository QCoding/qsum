from setuptools import setup, find_packages

MAJOR = 0
MINOR = 0
PATCH = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)

packages = find_packages()

setup(
    name="qsum",
    version=VERSION,
    packages=packages,
    url="https://github.com/QCoding/qsum",
    description="Intuitive and extendable checksumming for python objects",
)
