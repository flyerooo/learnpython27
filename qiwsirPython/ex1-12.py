#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/4 10:24

#!/usr/bin/env python
# coding:utf-8
# Created by Jeff on 2016/3/6 16:18

#10、自动售货机找零。通过键盘选中商品，并输入向自动售货机提交的金额，则显示出该找回的零钱。精确到分。
# 用户要能看到商品名称和单价
# 用户选择商品序号和购买数量
# 提示用户输入金额
# 用户输入的金额精确到分
# 输出显示商品名称、购买数量、应付总额、输入数额、找零

automat = {1: ('Cola', 3.5), 2: ('Chutty', 3), 3:('Water', 2.5), 4: ('Juice', 4)}    # 商品信息

def displayGoodsInfo():
    for i, j in automat.items():
        print "序号{} 名称{} 价格{}元".format(i, j[0], j[1], )  # 商品名称和单价
    print '-' * 20
def changeMoney(getMoney,goodsMoney):
    change = getMoney - goodsMoney
    return format(change, ".2f")

def select(goodsCcode,goodsQuantity):
    goodsMoney = automat[goodsCcode][1] * goodsQuantity
    return format(goodsMoney,".2f")

def main():
    displayGoodsInfo()
    goodsCcode = int(raw_input("请选择你要的商品序号:"))
    goodsQuantity = int(raw_input("请选择你要的商品数量(默认一件):"))
    getMoney = float(raw_input("请输入金额"))
    print "商品名称 {}  购买数量 {}".format(goodsCcode, goodsQuantity)
    print "应付总额",select(goodsCcode,goodsQuantity),"元"
    print  "输入数额",getMoney,"元"
    print "找零",changeMoney(getMoney,goodsMoney),"元"
if __name__ == "__main__":
    main()


