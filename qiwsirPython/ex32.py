#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/20 17:05
def displayInput(dataList, sumData):
    '''display input info'''
    print "How many numbers will you enter?"
    print len(dataList)
    print "Enter ",len(dataList)," integers, one per line."
    for i in dataList:
        print i
    print "The sum is ",sumData
def displayRate(dataList, sumData):
    '''display rate of each number'''
    print "The numbers are:"
    for i in dataList:
        print i,"which is ",format(float(i)/sumData,".3%"),"of the sum."
if __name__ =="__main__":
    data = int(raw_input("Enter an integer(the input ends if it is 0): "))
    dataList = []
    while data != 0:
        dataList.append(data)
        data = int(raw_input("Enter an integer(the input ends if it is 0): "))
    sumData = sum(dataList)
    displayInput(dataList, sumData)
    displayRate(dataList, sumData)
