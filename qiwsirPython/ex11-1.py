#!/usr/bin/env python
# coding:utf-8
# Created by Jeff on 2016/3/6 16:18
# 10、自动售货机找零。通过键盘选中商品，并输入向自动售货机提交的金额，则显示出该找回的零钱。精确到分。
# 用户要能看到商品名称和单价
# 用户选择商品序号和购买数量
# 提示用户输入金额
# 用户输入的金额精确到分
# 输出显示商品名称、购买数量、应付总额、输入数额、找零
"""
这个作业虽然能够完成了基本要求，但是，还有很大的改进余地。
１.写一个函数，输入的参数是用户输入金额和商品总价，然后输出找零结果
２、一个函数，专门负责接受用户选择商品序号和数量，并计算所需金额。
3.　商品类别用字典形式非常好。
建议这个题目按照上述建议从新做一下，然后在下次作业的时候发给我。
"""
automat = {1: ('Cola', 3.5), 2: ('Chutty', 3), 3:('Water', 2.5), 4: ('Juice', 4)}    # 商品信息
def displayGoodsInfo():
    for i, j in automat.items():
        print "序号{} 名称{} 价格{}元".format(i, j[0], j[1], )  # 商品名称和单价
    print '-' * 20

def changeMoney(total_goods_money):
    while True:
        try:
            custom_input_money = float(raw_input("请输入金额")) # 用户输入的金额
            while custom_input_money < total_goods_money:
                custom_input_money = float(raw_input("金额不足，请再投币: "))  + custom_input_money    #问题： 如果在这儿输入错误，又会从头循环，之前输入的钱就没了
            break
        except :
            print "输入错误"
    change = custom_input_money - total_goods_money
    return change

     return total_goods_money
def main():
    displayGoodsInfo()
    while True:
    try:
        goods_code = int(raw_input("请选择你要的商品序号:"))
        numbers_of_goods = int(raw_input("请选择你要的商品数量(默认一件):") or 1)
        if goods_code in automat.keys():
            break
        else:
            print "输入有误"
        break
    except ValueError:
        print "输入有误"
    total_goods_money = automat[goods_code][1] * numbers_of_goods

    custom1 = customSelection()

    print changeMoney(custom1)
    print "商品名称 {0}  购买数量{1}   应付总额{2}元   输入数额{3}元  找零{4}元".format(automat[custom1[0]][1], automat[1],b, b,b)