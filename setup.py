from os import path

from setuptools import setup, find_packages

MAJOR = 0
MINOR = 2
PATCH = 1
VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)

# https://packaging.python.org/guides/making-a-pypi-friendly-readme/
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


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
        dev_url="https://github.com/QCoding/qsum",
        summary="Python Checksumming Library",
        # in pkg-info this maps to 'summary'
        description="Intuitive and extendable checksumming for python objects",
        # in pkg-info this maps to 'description'
        long_description=long_description,
        long_description_content_type='text/markdown',
        python_requires='>=3.5',
        keywords="checksum checksumming hashing",
        tests_require=['pytest'],
        zip_safe=False,
        platforms="any",
        extras_require={
            "test": [
                "pytest>=4.4.0",
                "pytest-pylint",
            ]
        },
        classifiers=[
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
