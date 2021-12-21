#-*- coding: UTF-8 -*-
import sys
import re

#compile() 函数将一个字符串编译为字节代码，生成一个正则对象。当需要重复匹配的时候，效率更高
#\w+: 匹配多个字母、数字、下划线。等价于 [A-Za-z0-9_]，相当于匹配单词。
WORD_RE = re.compile(r'\w+') 
#构建一个空字典
index = {}
with open('file\ww.txt') as fp:
    #使用for循环逐行读取，使用enumerate()给每一行加一个索引。
    #enumerate()返回一个可迭代枚举对象（应该是一个迭代器），对象中是由多个元组组成，可拆包。
    for line_no,line in enumerate(fp,1):
        #对每一行进行正则匹配获取每一个单词，finditer()将获取的对象（一行）转换为迭代器，以便可以for循环。
        for match in WORD_RE.finditer(line):
            #group()用来提取分组截获的字符串,参数为0或者空则反回整个串，1、2...返回获取的对应位置的串。相当于正则里的()。
            #显然这里匹配的是每个单词
            word = match.group()
            #match.start()表示匹配的单词在匹配对象中的位置索引，这里表示单词列的位置。
            column_no = match.start()+1
            #单词的行和列位置
            location = (line_no,column_no)

            #方式一：使用get函数
            #获取word出现的情况，如果不存在，则返回一个空列表
            # occurrences = index.get(word,[])
            # #把单词的位置信息加入到列表中
            # occurrences.append(location)
            # #将位置列表添加到index字典中，key为单词，value为位置列表
            # index[word] = occurrences

            #方式二：使用setdefault
            index.setdefault(word, []).append(location)
            #上面语句等价于下面代码：
            # if word not in index:
            #     index[word] = []
            # index[word].append(location)       
        
#排序打印
for word in sorted(index,key=str.upper):
    print(word,index[word])