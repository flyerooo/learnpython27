#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/16 22:43
# 29、计算低于贫困线的家庭数量：
# income——家庭总收入
# size——家庭人口
# housing_cost——住房支出
# food_cost——食品支出
# 如果(housing_cost + food_cost * size) > (income / 2)，则该家庭为贫困家庭。
# 要求：
# 通过键盘输入若干个家庭的income、size、housing_cost、food_cost
# 计算低于贫困线的家庭数量，并打印显示。
class FamilyStatus(object):
    num = 0
    def __init__(self,income,size, housing_cost, food_cost):
        self.income = float(income)
        self.size = int(size)
        self.housing_cost = float(housing_cost)
        self.food_cost = float(food_cost)

    def poorFamily(self):
        if (self.housing_cost + self.food_cost * self.size) > self.income / 2:
            FamilyStatus.num += 1
        return FamilyStatus.num

if __name__ == "__main__":


    while True:
        income = raw_input("请输入家庭总收入(按q退出)：")
        if income == 'q':
            break
        size = raw_input("请输入家庭人口(按q退出)：")
        if size == 'q':
            break
        housing_cost = raw_input("请输入住房支出(按q退出)：")
        if housing_cost == 'q':
            break
        food_cost = raw_input("请输入食品支出(按q退出)：")
        if food_cost == 'q':
            break

        if income != 'q' and size != 'q' and housing_cost != 'q' and food_cost != 'q':
            a = FamilyStatus(income,size, housing_cost, food_cost)
            f = a.poorFamily()
    print "贫困家庭为：",f


