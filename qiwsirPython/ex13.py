#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/8 20:58
import re

def check():
    if string.endswith("?") == "?" and len(string) % 2 == 0: #偶数
        return "Yes"
    elif string.endswith("?") and len(string) % 2 == 1: #奇数
        return "No"
    elif string.endswith("!"):
        return "Wow"
    else:
        return "You always say " + string
if __name__ == "__main__":
    string = raw_input("请输入句子： ")
    print check()
