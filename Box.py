#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/7 8:11
class Box(object):
    num = 0
    def __init__(self):
        Box.num += 1
        self.length = 1
        self.width = 2
        self.hight = 3
        self._color = 'red'
        self.__volume = self.length * self.width * self.hight
        self.switch = "Close"
    def __get__(self, instance, owner):
        pass
    def __call__(self):
        return self.__volume

    def getVolume(self):
        return self.__volume
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    def getColor(self,color):
        self._color = color
        return self._color
    def turnOn(self):
        if self.switch ==  "Close":
            self.switch = "Open"
            return self.switch
        else:
            return "盒子已经打开,不能再次打开"
    def turnOff(self):
        if self.switch == "Open":
            self.switch = "Close"
        else:
            return "盒子已经关闭"
if __name__ == "__main__":
    a = Box()
    print a.turnOn()
    print a.turnOn()

