#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/6 11:22

def gcd(n1, n2):
    gcd = 1
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return gcd()