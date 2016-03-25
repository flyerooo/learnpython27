#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/7 15:51
class Rectangle(object):
    def __init__(self,width = 1, height = 2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return 2 * (self.width + self.height)
if __name__ == "__main__":
    aa = Rectangle(4, 40)
    bb = Rectangle(3.5 ,35.7)t
    print "aa's Area is", aa.getArea()
    print "aa's Perimeter is", aa.getPerimeter()
