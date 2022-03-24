#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

import warnings
import inspect

import osconfeed

DB_NAME = 'data/schedule2_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):  #用于测试
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

class MissingDatabaseError(RuntimeError):
    """ 需要数据库但没有指定数据库试抛出"""

class DbRecord(Record):   #Record的扩展类

    __db = None  #类属性，存储一个打开的 shelve.Shelf 数据库引用

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod 
    def get_db(): #静态方法，因为不管怎样调用，返回值始终是DbRecord.__db 引用的对象
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident): #类方法，在子类中易于定制它的行为
        db = cls.get_db()
        try:
            return db[ident] #从数据库中获取 ident 键对应的记录。
        except TypeError:
            if db is None:
                msg = "database not set; call '{}.set_db(my_db)'"
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:
                raise
    
    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super().__repr__()

class Event(DbRecord):

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)   #避免数据中有fetch字段

    @property
    def speaker(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speakers']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key)) 
                                    for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.name)
        else:
            return super().__repr__()


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls =  globals().get(cls_name, DbRecord)
        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)