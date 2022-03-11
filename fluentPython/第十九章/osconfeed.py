#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from urllib.request import urlopen
import warnings
import os
import json

URL = 'https://www.oreilly.com/pub/sc/osconfeed'
JSON = './data/osconfeed.json'

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        #在with语句中使用两个上下文管理器，分别用于读取和保存远程文件
        with urlopen(URL) as remote, open(JSON, 'wb') as local:  #python2.7和3.1之后可以这么干
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp) #解析JSON文件，返回Python原生对象


feed = load()