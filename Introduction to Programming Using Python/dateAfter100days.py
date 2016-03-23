#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/21 13:53
import random
# a = 'abcd23f'
# high = len(a) - 1
# reversedA=''
# while high >= 0:
#     reversedA += a[high]
#     high -= 1
# print reversedA
d =[]
for i in xrange(500):
    b = random.randint(0,19)
    d.append(b)
numItems = set(d)
numCounts = {}
print d
for num in d:
    if num in numCounts:
        numCounts[num] += 1
    else:
        numCounts[num] = 1
paris = list(numCounts.items())
print numCounts.items()
numList=[[value,key] for (key, value) in paris]
numList.sort()
for i in reversed(numList):
    print i