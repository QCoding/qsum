#!/bin/bash
# Build the pip package for qsum

# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build source distribution and wheel
python ../setup.py sdist bdist_wheel

echo "Package built successfully. Files are in the dist/ directory."
