from setuptools import setup, find_packages

MAJOR = 0
MINOR = 3
PATCH = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)


def setup_package():
    """Perform the setup for qsum"""
    packages = find_packages()

    metadata = dict(
        name="qsum",
        author="QCoding",
        author_email='quats111@gmail.com',
        license='MIT',
        version=VERSION,
        packages=packages,
        url="https://github.com/QCoding/qsum",
        # in pkg-info this maps to 'summary'
        description="Python Checksumming Library",
        # in pkg-info this maps to 'description'
        long_description=open("README.md", "r", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        python_requires='>=3.8',
        keywords="checksum checksumming hashing",
        tests_require=['pytest>=4.4.0', 'attrs', 'wheel'],
        zip_safe=False,
        platforms="any",
        extras_require={
            "test": [
                "pytest>=4.4.0",
                "pytest-pylint",
                "attrs",
                "wheel",
            ]
        },
        classifiers=[
            "Development Status :: 4 - Beta",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: Python :: 3.14",
            "Topic :: Scientific/Engineering",
        ]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
