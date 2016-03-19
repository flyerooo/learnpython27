#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/16 22:43
# 30、有五种鲜花，花名和价格，分别是：
# 牵牛花（petunia）：50
# 三色堇（pansy）：75
# 玫瑰（rose）：15
# 紫罗兰（violet）：50
# 康乃馨（carnation）：80
# 通过顾客购买的数量和花名，打印总价
class SellFlower(object):
    def __init__(self, petunia,pansy, rose, violet, carnation):
        self.petunia = 50 * petunia
        self.pansy = 75 * pansy
        self.rose = 15 * rose
        self.violet = 50 * violet
        self.carnation = 80 * carnation
    def amount(self):
        return self.petunia + self.pansy + self.rose +self.violet +self.carnation

if __name__ == "__main__":

    print"-----------------------"
    print "牵牛花（petunia）：50"
    print "三色堇（pansy）：75"
    print "玫瑰（rose）：15"
    print "紫罗兰（violet）：50"
    print "康乃馨（carnation）：80"
    print "-----------------------"
    petunia = int(raw_input("请输入牵牛花的数量："))
    pansy = int(raw_input("请输入三色堇的数量："))
    rose = int(raw_input("请输入玫瑰的数量："))
    violet = int(raw_input("请输入紫罗兰的数量："))
    carnation = int(raw_input("请输入康乃馨的数量："))
    a = SellFlower(petunia,pansy,rose,violet,carnation)

    print "总价为",a.amount()