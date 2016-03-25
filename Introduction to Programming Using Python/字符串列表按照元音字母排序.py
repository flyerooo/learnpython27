#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/17 23:47

by_string =['a', 'e', 'i', 'o', 'u']
words = ["suzhou", "shanghai", "hangzhou", "nanjing", "beijing"]

result = {}
for word in words:
    n = []
    for i in word:
        if i in by_string:
            n.append(by_string.index(i))
        else:
            n.append(9)
    result[word] = n
print result
vs = result.values()
print vs
vs.sort()
print vs
sorted_word = []
for i in vs:
    for k,v in result.items():
        if v == i:
            sorted_word.append(k)
print sorted_word