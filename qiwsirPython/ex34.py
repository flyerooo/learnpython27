#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/20 17:05
class SchoolKid(object):
    def __init__(self,):
        self.kidName = 'Jason'
        self.kidAge = 6
        self.teacherName = 'Paul'
        self.regards = 'Hi'
    def getKidName(self):
        return self.kidName
    def getKidAge(self):
        return self.kidAge
    def getTeacherName(self):
        return self.teacherName
    def getRegards(self):
        return self.regards
    def setKidName(self, kidName):
        self.kidName = kidName
    def setKidAge(self, kidAge):
        self.kidAge = kidAge
    def setTeacherName(self, teacherName):
        self.teacherName = teacherName
    def setRegards(self, regards):
        self.regards = regards
class ExaggeratingKid(SchoolKid):
    def getKidAge(self):
        return self.kidAge + 2
    def getRegards(self):
        return self.regards + " I am the best"
if __name__ == "__main__":
    a = ExaggeratingKid()
    print a.getRegards()
    print a.getKidAge()