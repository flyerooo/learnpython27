#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/9 8:21

def f(n):
    if n == 2:
        return 1
    return f(n - 1) + n - 1
if __name__ == "__main__":
    n = int(raw_input("请输入聚会人次: "))
    print n,"人参加聚会，共握手",f(n), '次'
