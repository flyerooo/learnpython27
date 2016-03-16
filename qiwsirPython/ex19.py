#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/6 21:15
class MotorBoat(object):
    def __init__(self, tankage = 20000, remainOil = 10000, maxSpeed = 200, currentSpeed, motoPower, disrance):
        self.tankage = tankage  #燃料箱的容量
        self.remainOil = remainOil  #燃料箱中的燃料数量
        self.maxSpeed = maxSpeed    #汽艇的最大速度
        self.currentSpeed = currentSpeed    # 汽艇的当前速度
        self.motoPower = motoPower  #马达的功率
        self.disrance = disrance    #航行的距离
    def setSpeed(self, speed): #修改汽艇的速度
        self.currentSpeed =  speed
    def getSpeed(self):  #在一定时间内以当前速度开行汽艇
        return self.currentSpeed
    def addOil(self, oil): #给汽艇加油
        self.remainOil += oil
    def getOil(self, time):  #返回燃料箱中燃料的数量
        self.remainOil = self.remainOil - self.motoPower * self.currentSpeed * 2 * time
        return self.remainOil
    def getDistance(self,time):  #返回目前为止汽艇航行的距离
        return self.currentSpeed * time
    # def getOilSubtract(self,time):
    #     self.oilSubstract = self.motoPower * self.currentSpeed * 2 * time

if __name__ == "__main__":
    aa = MotorBoat(20000, 10000, 200, 100, 10, 20)
    print "当前的速度为：",aa.getSpeed()
    print "燃料箱中的燃油量:",aa.getOil(2)
    print "航行的距离：",aa.getDistance(2)
    aa.addOil(200) # 加油
    aa.setSpeed(150) # 改变速度
    print "当前的速度为：",aa.getSpeed()
    # print "当前的速度为：",aa.getSpeed()
    print "燃料箱中的燃油量:",aa.getOil(0)
#这题还是不会做







