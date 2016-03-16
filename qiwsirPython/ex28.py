#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/16 22:43

#28、从键盘输入10个温度（代表10天的气温），计算平均温度，并且显示温度在平均温度之上的天数。

def temperature(t):
    averageTemperature = sum(t)/10.0
    return averageTemperature
def aboveAverageTemperature(t):
    higherTemperature = 0
    for i in t:
        if i > temperature(t):
            higherTemperature += 1
    return higherTemperature
if __name__ == "__main__":
    while True:
        t = eval(raw_input("请输入10个温度（逗号隔开）："))
        if len(t) == 10:
            break
        else:
            print "输入错误"
    print "平均温度为：",temperature(t)
    print "平均温度之上的天数为",aboveAverageTemperature(t),"天"