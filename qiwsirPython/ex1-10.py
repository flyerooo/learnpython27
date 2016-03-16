#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/3 11:12

automat = {1: ('Cola', 3.5), 2: ('Chutty', 3), 3:('Water', 2.5), 4: ('Juice', 4)}    # 商品信息

for i,j in automat.items():
       print "序号{} 名称{} 价格{}元".format(i,j[0],j[1],)        # 商品名称和单价
print '-'* 20
def returnChange(sumGoodsMoney):
    customInputMoney = 0
    while True:
        customInputMoney = float(raw_input("请投币:")) + customInputMoney
        change = customInputMoney - sumGoodsMoney
        if change < 0:
            print "输入金额不足"
        else:
            print "找零{}".format(change,".2f")
def userInput():
       while True:
            num = int(raw_input("请选择你要的商品序号:"))
            if num in automat.keys():
                break
            else:
                print "输入有误"
       quantity = int(raw_input("请选择你要的商品数量(默认一件):") or 1)
       sumGoodsMoney = automat[num][1] * quantity  #商品总价

def main():
    userInput()
    returnChange(userInput())
main()