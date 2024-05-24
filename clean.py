with open('README.md', 'rt') as f:
    text = f.read()
with open('README.md', 'wt') as f:
    f.write(text.replace('o', 'i'))
