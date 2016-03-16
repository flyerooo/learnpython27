#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/3 11:12

# 9、x>1，求最大整数k，使得2^k（2的k次幂）小于等于x
import sys
def main():
    while True:
        x = raw_input("请输入大于1的数(按q退出)：")
        if x.isdigit() and eval(x) > 1:   # 这个判断有点问题，小数不能用
            break
        elif x.lower() == 'q':
            print "退出程序"
            sys.exit()
        else:
            print "输入错误"
    k = 0
    while eval(x) >= 2 ** k:
        k += 1
    print "最大整数k为%d" % (k - 1)
main()