#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/7 14:06

class PersonAddress(object):
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number
    def getInfo(self):
        return self.name, self.email, self.number
    def setEmail(self, email):
        self.email = email
    def setNumber(self, number):
        self.number = number
if __name__ == "__main__":
    aa = PersonAddress("Jeff", "11111@gmail.com", 111111)
    print aa.getInfo()
    aa.setEmail("22222@gmail.com")
    aa.setNumber("222222")
    print aa.getInfo()