#-*- coding: UTF-8 -*-

from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
d_proxy[2]='B'