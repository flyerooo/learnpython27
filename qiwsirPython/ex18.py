#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/6 20:45
# 18、编写一个跟踪商品销售的类，这个类的对象将拥有如下属性：
# 销售数量
# 销售总额
# 总折扣
# 每件商品的成本
# 批发数量
# 批发折扣百分比
# 并且拥有如下方法：
# registerＳale(n记录n件商品的销售，如果n大于批发数量，每件商品的成本将按照批发折扣下调。
# displaySale显示销售数量、总销售额以及总折扣
# 要求：
# 用python实现上述过程
# 编写测试数据进行测试

class Sale(object):
    def __init__(self,quantityOfSales, totalSales, totalDiscount,costValue, wholesaleNumber, wholesaleDiscount):
        self.quantityOfSales = quantityOfSales      # 销售数量
        self.totalSales = totalSales        # 销售总额
        self.totalDiscount = totalDiscount      # 总折扣
        self.costValue = costValue      # 每件商品的成本
        self.wholesaleNumber = wholesaleNumber      # 批发数量
        self.wholesaleDiscount = wholesaleDiscount      # 批发折扣百分比
    def registerSale(self):
        if self.quantityOfSales > self.wholesaleNumber:
            self.costValue *= self.wholesaleDiscount
    def displaySale(self):
        self.registerSale()
        self.totalDiscount += self.quantityOfSales * self.wholesaleDiscount # 没太搞清每件商品的成本将按照批发折扣下调的意思
        print "销售数量",self.quantityOfSales
        print "总销售额",self.totalSales
        print "总折扣",self.totalDiscount
if __name__ == "__main__":
    aa =Sale(100, 200, 30, 50, 40, 0.80) # 销售数量200，批发数量40
    aa.displaySale()
    bb =Sale(100, 44, 30, 50, 200, 0.80)
    bb.displaySale()
# 面向对象编程感觉还不会做

