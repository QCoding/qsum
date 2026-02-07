import os

# Define paths relative to this file
# qsum/util/_paths.py -> qsum/util -> qsum -> root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(REPO_ROOT, 'qsum', 'types.csv')
MD_PATH = os.path.join(REPO_ROOT, 'TYPES.md')
