#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

charles = {'name': 'Charles L. Dodgson', 'born': 1832}
#lewis是charles的别名
lewis = charles
print(lewis is charles)
print(id(charles),id(lewis))

#结果
#True
#2409883719808 2409883719808

#给lewis添加一个元素相当于向charles添加一个元素
lewis['balance'] = 950
print(charles)

#结果
#{'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

#----------------------------------------------------------------
#冒充者
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
#比较两个对象，结果相等，这是因为 dict 类的 __eq__ 方法就是这样实现的
print(alex == charles) 
#但它们是不同的对象
print(alex is charles)

#结果：
#True
#False