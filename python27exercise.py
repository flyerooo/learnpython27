#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/3 11:12

automat = {1: ('Cola', 3.5), 2: ('Chutty', 3), 3:('Water', 2.5), 4: ('Juice', 4)}    #
def displayGoodsInfo():
    for i,j in automat.items():
           print "序号{} 名称{} 价格{}元".format(i,j[0],j[1],)        # 商品名称和单价
    print '-'* 20
def change(customMoney, goodsMoney):
    return format((customMoney - goodsMoney), ".2f")
def goodsMoney(goodsCode, goodsNum):
    return automat[goodsCode][1] * goodsNum



if __name__ == "__main__":
    displayGoodsInfo()
    goodsCode = int(raw_input("请选择你要的商品序号: "))
    goodsNum = int(raw_input("请选择你要的商品数量: "))
    print "商品金额：",format((automat[goodsCode][1] * goodsNum),'元'
    customMoney = float(raw_input("请投币:"))
    print "找零",change(customMoney, goodsMoney(goodsCode, goodsNum))