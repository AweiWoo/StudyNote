#!/usr/bin/python
# -*- coding:UTF-8 -*-
# author: wwu

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
            #直接调用策略函数
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


#显示的指定
#promos = [fidelity_promo, bulk_item_promo, large_order_promo]

#使用装饰器
promos = [] 

def promotion(promo_func): 
    promos.append(promo_func)
    return promo_func

#使用函数实现各个策略
@promotion
def fidelity_promo(order):
    if order.customer.fidelity >= 1000:
        return order.total() * 0.05
    else:
        return 0

@promotion
def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >=20:
            discount += item.total() * .1
    return discount

@promotion
def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    return max(promo(order) for promo in promos)

if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),LineItem('apple', 10, 1.5),LineItem('watermellon', 5, 5.0)]
    #print(globals())
    print(Order(joe, cart, best_promo))