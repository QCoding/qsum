from setuptools import setup, find_packages

MAJOR = 0
MINOR = 1
PATCH = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)


def setup_package():
    """Perform the setup for qsum"""
    packages = find_packages()

    metadata = dict(
        name="qsum",
        author="Justin M. Quartiere",
        license='MIT',
        version=VERSION,
        packages=packages,
        url="https://github.com/QCoding/qsum",
        description="Intuitive and extendable checksumming for python objects",
        summary="Python Checksumming Library",
        python_requires='>=3.5',
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
