#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/21 23:18
# 36、编写一个程序，计算两个整数相除后的余数。要求用户输入两个整数，分别作为被除数和除数。捕获抛出的任何异常，并让用户输入新值。

def remainder(dividend,divisor):
    return dividend % divisor

if __name__ == "__main__":
    while True:
        try:
            dividend = int(raw_input("Enter a dividend: "))
            divisor = int(raw_input("Enter a divisor: "))
            num = remainder(dividend,divisor)
            break
        except ValueError:
            print "ValueError, please enter again"
        except ZeroDivisionError:
            print "ZeroDivisionError, please enter again"
        except:
            print "Something wrong in the input,please enter again"
    print dividend,' % ',divisor,' = ',num