#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/13 23:57
# 24、写一个程序，计算二元一次方程组的根。
import math
def function(a, b, c):
    x1 = None
    x2 = None
    if b ** 2 - 4 * a * c >= 0:
        x1 = (-b - math.sqrt(b ** 2 - 4 * a * c))/ 2 * a
        x2 = (-b + math.sqrt(b ** 2 - 4 * a * c))/ 2 * a
        return x1, x2
    else:
        return "方程无实数根"
if __name__ == "__main__":
    print "一元二次方程a * x ** 2 + b * x + c = 0"
    a = float(raw_input("请输入a的值:"))
    b = float(raw_input("请输入b的值:"))
    c = float(raw_input("请输入c的值:"))
    print "x1,x2 =",function(a, b, c)