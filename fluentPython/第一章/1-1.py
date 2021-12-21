#-*- coding: UTF-8 -*-
import collections

#namedtuple可以用以构建只有少数属性但是没有方法的对象。
Card = collections.namedtuple('Card',['rank','suit']) #rank 牌面大小 suit 花色
#type 是所有内置对象或者类的基类型,上面Card返回的就是一个type类型

class FrenchDeck:
    #注意这个地方为什么要用str函数，因为后面要使用index()函数
    ranks = [str(n) for n in range(2,11)] + list('JQKA')  #返回一个列表
    suits = 'spades diamonds clubs hearts'.split()  # 依然返回一个列表
             #spades:黑桃 diamonds:方块 clubs:梅花 hearts: 红桃

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits 
                                    for rank in self.ranks]
        # self._cards = []
        # for suit in self.suits:
        #     for rank in self.ranks:
        #         self._cards.append(Card(rank, suit))

    #有了这个特殊方法，那么对象可以直接使用len()来求长度
    def __len__(self):
        return len(self._cards)

    #有了这个特殊方法，那么类对象就可以支持切片操作,而且可以迭代
    def __getitem__(self,position):
        return self._cards[position]

# #初始化一张牌
# beer_card = Card('7','diamonds')
# print beer_card
# #查看这些对象的类型
# print type(Card)
# print type(beer_card)

#实例化一个FrenchDeck对象（一副有顺序的扑克牌）
deck = FrenchDeck()
#查看这个对象
# print len(deck)
#print deck.ranks
# print deck.suits

# #一叠牌中抽取特定的牌
# print deck[0]
# print deck[-1]

# #随机抽取一张牌
# from random import choice
# print choice(deck)

# #切片操作
# print deck[:3]

# #迭代操作
# for card in deck:
#     print card
# #反向迭代
# for card in reversed(deck):
#    print card

suits_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    #获取一种花色牌的索引（0-12）
    rank_value = FrenchDeck.ranks.index(card.rank) #查询一张牌的面值
    #['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'].index('2')
    #使用下面方法计算一种权重
    return rank_value * len(suits_values) + suits_values[card.suit]
print '-------------------------'
#deck对象中的值（Card(rank='J', suit='hearts')）作为参数传递给spades_high函数
for card in sorted(deck,key=spades_high):
    print card

#知识点：
#  1、namedtuple的作用
#  2、type与object的关系
#  3、列表生成式
#  4、random模块
#  5、index(),sorted()
#  6、super()

#特殊方法的存在主要是为了被python解释器调用，我们自己不需要过多的使用它们。
#但在写我们自己的类的时候，可以适当的定义一些特殊方法，使我们的代码更加的健壮。