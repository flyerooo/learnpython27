#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/1 21:27

# 49、自定义一个类，要求输入任何一个浮点数，都能输出一个经过四舍五入
# 后保留两位小数的数值。

class RoundFloat(object):
    def __init__(self, round_float):
        self.round_float = round(round_float,2)
    def __str__(self):
        return str(self.round_float)

if __name__ == "__main__":
    a = RoundFloat(5.432)
    print a
# 还是没弄懂__str__,__repr__意义在哪，不用它应该也没什么问题吧