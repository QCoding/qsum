import csv
import os
from qsum.util._paths import CSV_PATH, MD_PATH

def test_types_md_is_up_to_date():
    """
    Verifies that TYPES.md is up-to-date with qsum/types.csv.
    If this test fails, run `python scripts/generate_types_md.py` to update the documentation.
    """
    assert os.path.exists(CSV_PATH), f"CSV file not found at {CSV_PATH}"
    assert os.path.exists(MD_PATH), f"Markdown file not found at {MD_PATH}"

    # Generate expected markdown content
    with open(CSV_PATH, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        rows = list(reader)

    expected_lines = ['# Supported Types\n', '\n']
    expected_lines.append('| ' + ' | '.join(headers) + ' |\n')
    expected_lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |\n')

    for row in rows:
        escaped_row = [cell.replace('|', '\\|') for cell in row]
        expected_lines.append('| ' + ' | '.join(escaped_row) + ' |\n')

    expected_content = ''.join(expected_lines)

    # Read actual markdown content
    with open(MD_PATH, 'r') as mdfile:
        actual_content = mdfile.read()

    assert actual_content == expected_content, \
        "TYPES.md is not up-to-date with qsum/types.csv. Please run `python scripts/generate_types_md.py`."
