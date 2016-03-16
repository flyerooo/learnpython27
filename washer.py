#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/8 0:19

class Washer(object):
    def __init__(self, water = 10, scour = 2):
        self._water = water
        self.scour = scour
        self.year = 2010
    @property
    def water(self):
        return self._water
    @water.setter
    def water(self, water):
        if 0 < water <= 500:
            self._water = water
        else:
            print "set Failure!"
    @property
    def total_year(self):
        return 2015 - self.year
    @classmethod
    def get_washer

    def set_water(self, water):
        self.water = water
    def set_scour(self, scour):
        self.scour = scour
    def add_water(self):
        print "Add water: ",self.water
    def add_water(self):
        print "Add water:",self.water
    def add_scour(self):
        print "Add water:",self.scour
    def start_wash(self):
        self.add_water()
        self.add_scour()
        print "Start wash..."
if __name__ == "__main__":
    w = Washer()
    print w.water
    w.water = -123
    print w.water
    print w.total_year
