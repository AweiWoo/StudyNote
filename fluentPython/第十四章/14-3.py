#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import itertools

#-------------------------用于过滤的生成器函数-------------------------
# 从输入的可迭代对象中产出元素的子集，而且不修改元素本身
def vowel(c):
    return c.lower() in  'aeiou'

list(filter(vowel, 'Aardvark')) #['A', 'a', 'a']
#filterfalse与filter作用相反
list(itertools.filterfalse(vowel, 'Aardvark')) #['r', 'd', 'v', 'r', 'k']
#遇到真值继续，遇到假值停止，产出后面元素
list(itertools.dropwhile(vowel, 'Aardvark')) #['r', 'd', 'v', 'a', 'r', 'k']
#与dropwhile相反，返回真值产出元素，遇到假值立即停止
list(itertools.takewhile(vowel, 'Aardvark'))  #['A', 'a']
#对应比较两个迭代对象，真值返回
list(itertools.compress('Aardvark', (1,0,1,1,0,1))) #['A', 'r', 'd', 'a']
#类似于[:4]
list(itertools.islice('Aardvark', 4))  #['A', 'a', 'r', 'd']
#类似于[4:7]
list(itertools.islice('Aardvark', 4,7))  #['v', 'a', 'r']
#类似于[1:7:2]
list(itertools.islice('Aardvark', 1,7,2)) #['a', 'd', 'a']


#------------------------用于映射的生成器函数--------------------------
# 在输入的单个可迭代对象中的各个元素上做计算，然后返回结果 ,map 和starmap 例外，他们处理多个可迭代的对象
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
#一个参数，前两个元素相加，计算结果与下个元素相加，一次类推
list(itertools.accumulate(sample)) #[5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
#两个参数，第二个参数为函数。计算最小值
list(itertools.accumulate(sample, min)) #[5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
#计算最大值
list(itertools.accumulate(sample, max)) #[5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
#产出由两个函数组成的元组
list(enumerate('abc', 1)) #[(1, 'a'), (2, 'b'), (3, 'c')]
import operator
list(map(operator.mul, range(11), range(11))) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list(map(operator.mul, range(11), [2, 4, 8])) #[0, 4, 16]
list(map(lambda a, b: (a, b), range(11), [2, 4, 8])) #[(0, 2), (1, 4), (2, 8)]
#starmap的第二个参数必须要能产出可迭代对象，然后将产出的可迭代对象在第一个函数参数中应用
list(itertools.starmap(operator.mul, enumerate('abcde', 1))) #['a', 'bb', 'ccc', 'dddd', 'eeeee']
list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))) 
#[5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.888888888888889, 4.5]


#-----------------------用于合并的生成器函数--------------------------
# 这些函数都从输入的多个可迭代对象中产出元素
# chain用来对可迭代对象产出的元素进行拼接
list(itertools.chain('ABC', range(2))) #['A', 'B', 'C', 0, 1]
list(itertools.chain(enumerate('ABC'))) #[(0, 'A'), (1, 'B'), (2, 'C')]
list(itertools.chain.from_iterable(enumerate('ABC'))) #[0, 'A', 1, 'B', 2, 'C']

#zip 常用于把两个可迭代的对象合并成一系列由两个元素组成的元组
list(zip('ABC', range(5))) #[('A', 0), ('B', 1), ('C', 2)]
list(zip('ABC', range(5), [10, 20, 30, 40])) #[('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]

# zip_longest中所有可迭代对象都会处理到头，如果需要会填充 None
list(itertools.zip_longest('ABC', range(5))) #[('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
list(itertools.zip_longest('ABC', range(5), fillvalue='?')) #[('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]

#itertools.product用来计算笛卡尔积
list(itertools.product('ABC', range(2))) #[('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
list(itertools.product('ABC')) #[('A',), ('B',), ('C',)]
# repeat=N 关键字参数告诉 product 函数重复 N 次处理输入的各个可迭代对象
# repeat=2 相当于：itertools.product('ABC', 'ABC')
list(itertools.product('ABC', repeat=2)) 
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
list(itertools.product(range(2), repeat=3))
#[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]


#--------------从一个元素中产出多个值，扩展输入的可迭代对象------------------
#itertools模块中的count 和 repeat 函数返回的生成器：这两个函数都不接受可迭代的对象作为输入。
ct = itertools.count()
next(ct) #0
next(ct) #1
next(ct) #2
#使用 islice 或 takewhile 函数做了限制，可以从 count 生成器中构建列表
list(itertools.islice(itertools.count(1, 0.3), 3))  #[1, 1.3, 1.6]

#cycle 生成器会备份输入的可迭代对象，然后重复产出对象中的元素
cy = itertools.cycle('ABC')
next(cy) #A
next(cy) #B
next(cy) #C
#只有受到 islice 函数的限制，才能构建列表
list(itertools.islice(cy, 7)) #['A', 'B', 'C', 'A', 'B', 'C', 'A']
#构建一个 repeat 生成器，始终产出数字 7
rp = itertools.repeat(7)
next(rp) #7
next(rp) #7
next(rp) #7
#第二个参数，指定产出同一个元素的次数
list(itertools.repeat(8, 4)) #[8, 8, 8, 8]
list(map(operator.mul, range(11), itertools.repeat(5))) #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# 在 itertools 模块的文档中combinations、combinations_with_replacement和 permutations 生成器函数，
# 连同 product 函数，称为组合学生成器（combinatoric generator）。
# itertools.product 函数和其余的组合学函数有紧密的联系。

#combinations(it, out_len)：it 产出的 out_len 个元素组合在一起，然后产出
list(itertools.combinations('ABC', 2)) #[('A', 'B'), ('A', 'C'), ('B', 'C')]
#与combinations一样，但包含相同元素的组合
list(itertools.combinations_with_replacement('ABC',2)) 
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


#------------------用于重新排列的生成器函数-------------------------
#itertools.groupby 和 itertools.tee 返回多个生成器
list(itertools.groupby('LLLLAAGGG'))
# [('L', <itertools._grouper object at 0x000001F31C8E44C0>), 
# ('A', <itertools._grouper object at 0x000001F31C8E4400>), 
# ('G', <itertools._grouper object at 0x000001F31C8E42E0>)]
for char, group in itertools.groupby('LLLLAAGGG'):
    print(char, '->', list(group))
# L -> ['L', 'L', 'L', 'L']
# A -> ['A', 'A']
# G -> ['G', 'G', 'G']

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear','bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(animals) #['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin']

for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))
# 3 -> ['rat', 'bat']
# 4 -> ['duck', 'bear', 'lion']
# 5 -> ['eagle', 'shark']
# 7 -> ['giraffe', 'dolphin']

#内置的reversed函数，不接受可迭代对象，而只接受序列为参数
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))
# 7 -> ['giraffe', 'dolphin']
# 7 -> ['dolphin', 'giraffe']
# 5 -> ['shark', 'eagle']
# 4 -> ['lion', 'bear', 'duck']
# 3 -> ['bat', 'rat']

#itertools.tee 从要给可迭代对象中产出多个生成器，每个生成器都可以产出输入的给个元素，默认2个
list(itertools.tee('ABC', 3))
#[<itertools._tee object at 0x0000025F5EDC18C0>, <itertools._tee object at 0x0000025F5EDC1900>, <itertools._tee object at 0x0000025F5EDC1640>]
g1, g2, g3 = itertools.tee('ABC', 3)
next(g1) #A
next(g2) #A
next(g3) #A
next(g1) #B
list(g2) #['B', 'C']
list(zip(*itertools.tee('ABC'))) #[('A', 'A'), ('B', 'B'), ('C', 'C')]
list(zip(*itertools.tee('ABC',3))) #[('A', 'A', 'A'), ('B', 'B', 'B'), ('C', 'C', 'C')]

# 注意，这一节的示例多次把不同的生成器函数组合在一起使用。这是这
# 些函数的优秀特性：这些函数的参数都是生成器，而返回的结果也是生
# 成器，因此能以很多不同的方式结合在一起使用