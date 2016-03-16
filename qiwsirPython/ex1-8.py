#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/3 11:12



# 8、获取当前日期，并计算当前日期距离1998年5月1日由多少天、多少周（取整）、多少月（取整）、几个季度（取整）、几年（取整）。
from datetime import date
def main():
    #获取当前日期
    now = date.today()
    d1 = date(1998, 5, 1)
    #间隔天数
    days_diff = (now - d1).days
    #间隔星期数
    weeks_diff = days_diff / 7
    #间隔月数
    months_diff = (now.year - d1.year) * 12 + (now.month - d1.month) if now.day >= d1.day else (now.year - d1.year) * 12 + (now.month - d1.month) - 1
    #间隔年数
    years_diff = months_diff / 12


    print r"今天距离1998年 5月 1日共：",days_diff,"天"
    print r"今天距离1998年 5月 1日共：",weeks_diff,"周"
    print r"今天距离1998年 5月 1日共：",months_diff,"月"
    print r"今天距离1998年 5月 1日共：",years_diff,"年"
main()
#我试着自己用if/else算闰年，有没有二月的情况等，然后再计算，但发现很复杂，就只能这样算了