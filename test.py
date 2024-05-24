import sys


with open('README.md') as f:
    if 'uhoh' in f.read():
        sys.exit(1)
