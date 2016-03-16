#!/usr/bin/env python
#coding:utf-8
#Created by one on 2016/2/27

__metaclass__ = type

class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print "{} is about {}".format(name, self.height)
    def eye(self):
        print "eye is big"

class Girl(Person):
    def __init__(self):
        super(Girl, self).__init__()#在子类中，没有建立父类的实例，却要是用父类的方法，即非绑定方法
        self.breast = 90

    def about(self, name):
        print "{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast)
        Person.about(self,name)#调用父类的about方法


if __name__ == "__main__":
    cang = Girl()
    cang.about("canglaoshi")
