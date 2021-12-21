#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from collections import namedtuple
metro_data = [
    ('Tokyo','JP',36.933,(35,139)),
    ('Delhi NCR','IN',21.935,(28,77)),
    ('Mexico City','MX',20.142,(40,-74))
]
Latlog = namedtuple('Latlog','lat long') # 等价于Latlog = namedtuple('Latlog',['lat','long'])
Metropolis = namedtuple('Metropolis','name cc pop coord')
print(Latlog.__doc__)
print(Metropolis.__doc__)
#这里可以看作namedtuple（具名元组）中嵌套了namedtuple
metro_areas = [Metropolis(name,cc,pop,Latlog(lat, long)) for name,cc,pop,(lat,long) in metro_data]
print(metro_areas[0])

from operator import attrgetter
#定义一个attrgetter，获取name,cc,以及嵌套的lat属性，现在要使用metro_areas中嵌套的coord中的lat字段进行排序
name_lat = attrgetter('name','cc','coord.lat')
for city in sorted(metro_areas,key=attrgetter('coord.lat')):
    print(name_lat(city))