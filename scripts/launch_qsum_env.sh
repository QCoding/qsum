#!/bin/bash
# Script to create a fresh Python environment with qsum from PyPI

set -e

ENV_NAME="qsum_test_env"
ENV_DIR="./${ENV_NAME}"

echo "Creating fresh Python environment..."
python3 -m venv "${ENV_DIR}"

echo "Activating environment..."
source "${ENV_DIR}/bin/activate"

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing qsum from PyPI..."
pip install qsum

echo "Installing ipython..."
pip install ipython

echo ""
echo "Environment ready! Launching IPython..."
echo "You can import qsum and start using it."
echo ""

ipython
