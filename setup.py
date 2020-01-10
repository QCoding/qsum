from setuptools import setup, find_packages

MAJOR = 0
MINOR = 2
PATCH = 2
VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)


def setup_package():
    """Perform the setup for qsum"""
    packages = find_packages()

    metadata = dict(
        name="qsum",
        author="QCoding",
        license='MIT',
        version=VERSION,
        packages=packages,
        url="https://github.com/QCoding/qsum",
        dev_url="https://github.com/QCoding/qsum",
        # in pkg-info this maps to 'summary'
        description="Python Checksumming Library",
        # in pkg-info this maps to 'description'
        long_description="Intuitive and extendable checksumming for python objects",
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
            "Development Status :: 4 - Beta",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Scientific/Engineering",
        ]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
