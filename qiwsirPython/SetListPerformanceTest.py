#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/27 20:24

import random
import time
NUMBER_OF_ELEMENTS =10000
lst = list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)
s =set(lst)
startTime = time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in s
endTime = time.time()
runTime = int((endTime - startTime) *1000)

print "To test if",NUMBER_OF_ELEMENTS,"elements are in the set\n","The runtime is",runTime,"milliseconds"

startTime =time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in lst
endTime =time.time()
runTime = int((endTime - startTime) *1000)
print "\nTo test if",NUMBER_OF_ELEMENTS,"elements are in the list\n","The runtime is",runTime,"milliseconds"

startTime =time.time()
for i in range(NUMBER_OF_ELEMENTS):
    s.remove(i)
print s
endTime =time.time()
runTime = int((endTime - startTime) *1000)
print "To remove",NUMBER_OF_ELEMENTS,"elements are in the set\n","The runtime is",runTime,"milliseconds"

startTime =time.time()
for i in range(NUMBER_OF_ELEMENTS):
    lst.remove(i)
print lst
endTime =time.time()
runTime = int((endTime - startTime) *1000)
print "To remove",NUMBER_OF_ELEMENTS,"elements are in the list\n","The runtime is",runTime,"milliseconds"

