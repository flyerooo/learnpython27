#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/1

'''我大概知道插入，选择，冒泡排序原理大概是怎么回事,但程序就是写不出，
看教程上的这几个程序看了几个小时了，但还是不懂。
这三个程序是不是面试一般会考？我干脆背下来算了，真是没办法。
'''
#选择排序
def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = lst[i]
        currentMinIndex = i
        for j in range(i + 1, len(lst)):
            if currentMin > lst[i]:
                currentMin = lst[j]
                currentMinIndex = j
            if currentMinIndex != i:
                lst[currentMinIndex] = lst[i]
                lst[i] = currentMin
    return lst
#插入排序
def insertionSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1
        lst[k + 1] = currentElement
    return lst

#冒泡排序省略,反正只能抄

if __name__ == "__main__":
    s = raw_input("输入5个数字用空格隔开: ")
    items = s.split()
    lst = [eval(x) for x in items]
    print insertionSort(lst)