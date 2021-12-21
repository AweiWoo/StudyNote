#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

def tag(name,*content,cls=None,**attrs):
    """生成一个或多个html标签
       参数：
        name: 标签名称
        content: 标签类容
        cls: 标签元素类名，此参数位仅限关键字参数
        attrs: 标签属性
    """
    if cls is not None:
        #标签元素类名也属于标签的属性，如果class非空，则将其写入到attrs中
        attrs['class'] = cls
    if attrs:
        #属性拼接
        attr_str = ''.join(' %s="%s"' % (attr,value) for attr,value in sorted(attrs.items()))
    else:
        attr_str = ''  
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name,attr_str,c,name) for c in content)
    else:
        return '<%s%s />' % (name,attr_str)

#使用定位参数（name）
print(tag('br'))
#第一个参数后面的任意参数都会被**content捕获
print(tag('p','hello','world'))
#没有明确指定名称的关键字参数id=33会被**attrs捕获
print(tag('p','hello',id=33))
#cls参数是明确名称的关键字参数
print(tag('p','hello',cls='sidebar'))
print(tag('p','hello',cls='sidebar',id=33))
#name虽然是定位参数，但也可以通过关键字参数传入
print(tag(content='testing',name='img'))
print(tag('img',content='testing'))
#字典中所有元素作为单个参数传入，同命键会绑定到对应的参数上，余下被**attrs捕获
my_tag = {'title':'Sunset Boulevard','src':'sunset.jpg','cls':'framed'}
print(tag('wuwei',**my_tag))
c=('a','b','c')
print(tag(*c,**my_tag))

from inspect import signature
sig=signature(tag)
print(sig)
for name,param in sig.parameters.items():
    print(param.kind,':', name, '=' , param.default)