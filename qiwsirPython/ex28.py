#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/16 22:43

#28、从键盘输入10个温度（代表10天的气温），计算平均温度，并且显示温度在平均温度之上的天数。
class AverageTemperature(object):
    def __init__(self, t):
        self.t = t
    def averageTemperature(self):
        self.average = sum(self.t)/10.0
        return self.average

    def aboveAverageTemperature(self):
        # higherTemperature = 0
        # for i in t:
        #     if i > temperature(t):
        #         higherTemperature += 1
        # return higherTemperature
        return len(filter((lambda a: a > self.average), self.t))
if __name__ == "__main__":
    t = eval(raw_input("请输入10个温度（逗号隔开）："))
    a = AverageTemperature(t)
    print "平均温度为：",a.averageTemperature()
    print "平均温度之上的天数为",a.aboveAverageTemperature(),"天"