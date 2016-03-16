#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/8 20:16

class BMI(object):
    """
    体质指数（BMI）=体重（kg）÷身高^2（m）
    过轻：低于18.5
    正常：18.5-24.99
    过重：25-28
    肥胖：28-32
    非常肥胖, 高于32
    """
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    def getBMI(self):
        BMI = self.weight / (self.height ** 2)
        return round(BMI,1)
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "过轻"
        elif bmi < 24.99:
            return "正常"
        elif bmi < 28:
            return "过重"
        elif bmi < 32:
            return "肥胖"
        else:
            return "非常肥胖"
if __name__ == "__main__":
    weight = float(raw_input("请输入体重(公斤): "))
    height = float(raw_input("请输入身高(米): "))
    person = BMI(weight, height)
    print "你的BMI为：",person.getBMI(),"你的体重：",person.getStatus()


