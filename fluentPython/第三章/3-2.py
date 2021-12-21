#-*- coding: UTF-8 -*-
import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

#将映射对象index中的key的类型设置为list，但查找的key不存在的时候，创建对应key的值为一个空列表。
index = collections.defaultdict(list)
with open('file\ww.txt') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no,column_no)
            #index中key在collections.defaultdict作用下，已经时list，可以直接使用append
            index[word].append(location)


for word in sorted(index,key=str.upper):
    print(word,index[word])