#! /usr/bin/env python
#coding:utf-8
#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/23 20:33#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/21 23:18

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
            print ("ValueError, please enter again")
        except ZeroDivisionError:
            print ("ZeroDivisionError, please enter again")
        except:
            print ("Something wrong in the input,please enter again")
    print ("{} % {} = {}".format(dividend, divisor, num))#!/usr/bin/env python
#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/23 20:33#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/21 23:18

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
            print ("ValueError, please enter again")
        except ZeroDivisionError:
            print ("ZeroDivisionError, please enter again")
        except:
            print ("Something wrong in the input,please enter again")
    print ("{} % {} = {}".format(dividend, divisor, num))#!/usr/bin/env python
