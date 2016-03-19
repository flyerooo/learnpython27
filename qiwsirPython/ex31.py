#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/16 22:43
# 31、记录商店的销售情况：
# 键盘输入商店商品单价、数量
# 每天销售的商品数量和单价都不完全一样
# 最终计算，通过键盘输入的那几天的销售总额。


class SellTrace(object):
    sum = 0
    def __init__(self,price, num):
        self.price = float(price)
        self.num = int(num)
        SellTrace.sum += self.price * self.num
    def amount(self):

        return SellTrace.sum
if __name__ == "__main__":
    while True:
        price = raw_input("商品单价(按q退出)：")
        if price == 'q':
            break
        num = raw_input("商品数量：")
        a = SellTrace(price, num)

    print "销售总额为：",a.amount()