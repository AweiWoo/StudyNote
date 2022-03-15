#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

'''
>>> from osconfeed import load
>>> import shelve
>>> import schedule1
>>> db = shelve.open(schedule1.DB_NAME)
>>> if schedule1.CONFERENCE not in db:
...     schedule1.load_db(db)
...
F:\StudyNote\fluentPython\第十九章\schedule1.py:19: UserWarning: loading data/schedule1_db
  warnings.warn('loading ' + DB_NAME)
>>> speaker = db['speaker.157509']
>>> type(speaker)
<class 'schedule1.Record'>
#各个 Record 实例都有一系列自定义的属性，对应于底层 JSON 记录 里的字段。
>>> speaker.name, speaker.twitter
('Robert Lefkowitz', 'sharewaveteam')
>>> event = db['event.34505'] 
>>> type(event)
<class 'schedule1.Record'>
>>> event.name
"Why Schools Don't Use Open Source to Teach Programming"
#一定要记得关闭 shelve.Shelf 对象。如果可以，使用 with 块确保Shelf对象会关闭
>>> db.close()
'''

import warnings
import osconfeed

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs) #一个重要的做法：在 __init__ 方法中更新实例的 __dict__ 属性。


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key ='{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record) #构建Record实例，存储在数据库的key下