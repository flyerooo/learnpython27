#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/13 22:58

# 22、完全数，是对具有某种特征的整数的称呼。维基百科中，对完全数有非常准确的定义和解释。如下：
# 完全数，又稱完美數或完備數，是一些特殊的自然数：它所有的真因子（即除了自身以外的约数）的和，恰好等於它本身，完全数不可能是楔形數。
# 例如：第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3＝6，恰好等於本身。第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14＝28，也恰好等於本身。后面的数是496、8128。
# 关于完全数的更多内容，可以阅读：https://zh.wikipedia.org/zh/%E5%AE%8C%E5%85%A8%E6%95%B0
# 要求：编写一段Python程序，用其可以判断一个整数是否是完全数。

def perfectNumber(num):
    numTemp = num /2 + 1 #因子最大可能值
    divisorList = [1]
    divisor = 2
    #while divisor <= numTemp:
    for divisor in range(2, numTemp):
        if num % divisor == 0:
            divisorList.append(divisor)
        # divisor += 1
    print divisorList
    if num == sum(divisorList):
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(raw_input("请输入数字："))
    print num,perfectNumber(num)