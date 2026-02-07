import csv
import sys
import os

# Ensure we can import from qsum
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qsum.util._paths import CSV_PATH, MD_PATH

def generate_markdown(csv_path, md_path):
    with open(csv_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        rows = list(reader)

    with open(md_path, 'w') as mdfile:
        mdfile.write('# Supported Types\n\n')

        # Write table header
        mdfile.write('| ' + ' | '.join(headers) + ' |\n')
        mdfile.write('| ' + ' | '.join(['---'] * len(headers)) + ' |\n')

        # Write table rows
        for row in rows:
            # Escape pipes in content just in case
            escaped_row = [cell.replace('|', '\\|') for cell in row]
            mdfile.write('| ' + ' | '.join(escaped_row) + ' |\n')

if __name__ == '__main__':
    generate_markdown(CSV_PATH, MD_PATH)
    print(f"Generated {MD_PATH} from {CSV_PATH}")
