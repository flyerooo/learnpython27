#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/20 9:02
def isPalindrome(string):
    for i in range(len(string)):
        if string[i] == string[len(string) - i]:
            return True