# adapted from Alex Martelli's example in "Re-learning Python"
# http://www.aleax.it/Python/accu04_Relearn_Python_alex.pdf
# (slide 41) Ex: lines-by-word file index

# tag::INDEX[]
"""Build an index mapping word -> list of occurrences"""

import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}
print(sys.argv)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line): 
        #使用正则表达式对象 WORD_RE 在当前行 line 中查找所有匹配项并返回一个迭代器，match 迭代对象。 
            word = match.group() 
            #获取匹配到的单词。
            column_no = match.start() + 1 
            #获取单词在行中的起始位置，match.start() 返回匹配的起始位置，从 0 开始计数，所以加 1。
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)  # <1>

print(f'==================== \n match \n ====================: {match}')
print(word)

# display in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
# end::INDEX[]


#sys.argv 中以列表的形式存储了命令行中的输入
#sys.argv[0]为文件自身的名称,sys.argv[1]为后续第一个输入

'''
Python 的 re 包用于处理正则表达式(regular expressions),
提供了匹配字符串模式的功能。通过正则表达式,你可以对字符串执行复杂的匹配、搜索、替换等操作。

re 包的基本功能
匹配操作

re.match():从字符串的起始位置开始匹配,如果开头部分不匹配,返回 None。
re.search():搜索整个字符串,返回第一个匹配对象。
re.findall():返回所有非重叠的匹配对象,作为列表返回。
re.finditer():返回所有非重叠的匹配对象,作为迭代器返回。
替换操作

re.sub():替换字符串中的匹配项。
re.subn():替换字符串中的匹配项,并返回替换次数。
拆分字符串

re.split():根据匹配项拆分字符串。
re.compile() 函数
re.compile(pattern, flags=0) 函数用于编译正则表达式模式,返回一个模式对象,这个对象可以用于匹配字符串,提供比直接使用 re 函数更高效的多次匹配。

参数说明:

pattern: 要编译的正则表达式模式。
flags:可选参数,控制正则表达式的匹配方式,比如忽略大小写、多行匹配等。
使用 re.compile() 函数可以提高效率,特别是在需要多次使用相同正则表达式模式的时候。

r'\w+' 的含义
正则表达式模式 r'\w+' 的解释如下:

r:表示原始字符串(raw string),避免反斜杠 \ 转义。
\w:匹配任意字母、数字或下划线字符(相当于 [a-zA-Z0-9_])。
+:表示前面的字符或子模式重复一次或多次(即至少出现一次)。
因此,r'\w+' 可以匹配一个或多个字母、数字或下划线的序列。
'''