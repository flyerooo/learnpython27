#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/23 20:33
# 43、编写实现斐波那契数列的程序。（有多种实现方法，必须编写函数。建议至少写两种。
# 其中一种用递归实现。建议要自己研究，尽可能不上网搜索。因为这个题目非常常见。如果你写好了，
# 再上网搜索，对照修改是可以的。）

def fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n -2)
'''只能想到递归的写法，fibonacci2为参考网络代码'''
def fibonacci2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    for i in range(20):
        print fibonacci2(i),
    print '\t'
    for i in range(20):
        print fibonacci1(i),

