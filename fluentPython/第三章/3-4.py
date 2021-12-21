#-*- coding: UTF-8 -*-
import collections
class StrKeyDict(collections.UserDict):

    def __missing__(self,key):
        if isinstance(self,key):
            raise KeyError(key)
        return self[str(key)]
    #不需用self.key()，只需要self.data查询即可，所有的键都已经存储为字符串了。
    def __contains__(self,key):
        return str(key) in self.data
    def __setitem__(self,key,item):
        #把所有的键都转化为字符串
        self.data[str(key)] = item