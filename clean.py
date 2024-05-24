with open('README.md', 'rt') as f:
    text = f.read()
with open('README.md', 'wt') as f:
    if 'nocte' in text:
        text = text.replace('nocte', 'mane')
    else:
        text = text.replace('mane', 'nocte')
    f.write(text)
