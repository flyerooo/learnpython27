#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/20 17:05
# 35、创建类PayCalculator，拥有属性pay_rATE，以每小时人民币数量为单位。拥有方法compute_pay(hours)，计算给给定工作时间的报酬，并返回。
class PayCalculator(object):
    def __init__(self):
        self.pay_rate = 80
    def compute_pay(self,hours):
        return self.pay_rate * hours
if __name__ == "__main__":
    a = PayCalculator()
    print a.compute_pay(5)