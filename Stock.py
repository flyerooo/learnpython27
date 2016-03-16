#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/7 16:23

class Stock(object):
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
    def getName(self):
        return self.name
    def getSymbol(self):
        return self.symbol
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    def setPreviousClosingPrice(self, newPrice):
        self.__previousClosingPrice = newPrice
    def getCurrentPrice(self):
        return self.__currentPrice
    def setCurrentPrice(self,newCurrentPrice):
        self.__currentPrice = newCurrentPrice
    def getChangePercent(self):
        return (self.__previousClosingPrice - self.__currentPrice)/ self.__previousClosingPrice
if __name__ == "__main__":
    Create a rectangle with width 4 and height 40
    stock = Stock("Intel", "INTC", 20.5, 20.35)
    print("The price change is " + str(stock.getChangePercent()))