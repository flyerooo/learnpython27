#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/13 23:39

# 23、写一个程序，检查数N是否为素数。

def isPrime(num):
    primeTemp = num / 2
    divisor = 2
    while divisor <= primeTemp:
        if num % divisor == 0:
            return "不是素数"
        divisor += 1
    return "是素数"

num = int(raw_input("请输入数字："))
print num,isPrime(num)