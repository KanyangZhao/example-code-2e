import sys
from unicodedata import name

print(sys.version)
print()
print('sys.stdout.isatty():', sys.stdout.isatty())
print('sys.stdout.encoding:', sys.stdout.encoding)
print()

'''
在 Python 中，字符可以通过其 Unicode 名称进行引用，使用的是 \N{...} 这种形式。
这个形式称为 Unicode 转义序列。通过这种形式，你可以使用 Unicode 字符集中的特定字符，而不必记住它们的具体编码。
'''


test_chars = [
    '\N{HORIZONTAL ELLIPSIS}',       # exists in cp1252, not in cp437
    '\N{INFINITY}',                  # exists in cp437, not in cp1252
    '\N{CIRCLED NUMBER FORTY TWO}',  # not in cp437 or in cp1252
]

for char in test_chars:
    print(f'Trying to output {name(char)}:')
    print(char)
