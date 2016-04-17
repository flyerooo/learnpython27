#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/4/8 18:09

def composite(x, y):
    tuple_value = (x, y)
    return tuple_value

print map(composite, [1, 2, 3, 4], ['a', 'b', 'c', 'd', 'e'])
print zip([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])