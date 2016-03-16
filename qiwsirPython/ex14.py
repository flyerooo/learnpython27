#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/8 22:11

def ctof(digitTemp):
    return digitTemp * 1.8 + 32

def ftoc(digitTemp):
    return (digitTemp - 32) * 1.8

def main():

    while True:
        try:
            temp = raw_input("请输入摄氏/华氏温度（按q退出）：")
            if temp.lower() == 'q':
                break
            elif temp.lower().endswith('c') or temp.lower().endswith('f'):
                digitTemp = float(temp[:-2]) #温度数字部分
                if temp.lower().endswith('c'):
                    print temp, '=', ctof(digitTemp), 'F'
                elif temp.lower().endswith('f'):
                    print temp, '=', ftoc(digitTemp),'C'
            else:
                print '输入错误,',
        except ValueError:
            print '输入错误,',
if __name__ == "__main__":
    main()
