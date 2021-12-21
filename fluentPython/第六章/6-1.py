#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')  #消费者姓名和积分

class LineItem:

    def __init__(self, product, quantity, price):  #商品，数量，单价 
        self.product = product
        self.quantity = quantity
        self.price = price

    #单个商品总价
    def total(self):
        return self.price * self.quantity


class Order:  #根据上下文（哪个客户，积分，折扣类型）计算出折扣的价格

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion   #使用的折扣策略

    #计算所有商品总价
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    #计算折扣后的价格
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  #折扣策略

    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion):
    """积分为1000或以上的顾客提供5%折扣"""

    def discount(self, order):
        if order.customer.fidelity >= 1000:
            return order.total() * 0.05
        else:
            return 0


class BulkItemPromo(Promotion): 
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个或以上时提供7%折扣"""

    def discount(self, order):
        #使用集合set去重
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >10:
            return order.total() * 0.07
        return 0


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    #订单
    cart = [LineItem('banana', 30, 0.5), LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0), LineItem('orange', 20, 0.8), LineItem('strawberry', 20, 2.0)]

    #使用积分策略
    print(Order(joe, cart, FidelityPromo()))  #<Order total: 111.00 due: 111.00>
    print(Order(ann, cart, FidelityPromo()))  #<Order total: 111.00 due: 105.45>

    #使用单个商品数量到达20个策略
    print(Order(joe, cart, BulkItemPromo()))
    print(Order(ann, cart, BulkItemPromo()))

    #使用不同商品达到10个以上策略
    long_order = [ LineItem(str(item_code), 1,1.0) for item_code in range(10)]
    print(Order(joe, long_order, LargeOrderPromo()))
    print(Order(ann, cart, LargeOrderPromo()))


