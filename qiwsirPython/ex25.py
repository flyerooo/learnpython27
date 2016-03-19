#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/15 11:34
import profile
import datetime

starttime = datetime.datetime.now()
range1 = xrange(1, 10)
range2 = xrange(0, 10)
def f():
    for s in range1:
        for e in range2:
            if s == e:
                continue
            for n in range2:
                if n in [s, e]:
                    continue
                for d in range2:
                    if d in [s, e,n]:
                        continue
                    for m in range1:
                        if m in [s,e,n,d]:
                            continue
                        for o in range2:
                            if o in [s,e,n,d,m]:
                                continue
                            for r in range2:
                                if r in [s,e,n,d,m,o]:
                                    continue
                                for y in range2:
                                    if y in [s,e,n,d,m,o,r]:
                                        continue
                                    send = s*1000 + e*100 + n*10 + d
                                    more = m*1000 + o*100 + r*10 + e
                                    money = m*10000 + o*1000 + n*100 + e*10 + y
                                    if send + more == money:
                                        print "  %d%d%d%d" % (s, e, n, d)
                                        print " +%d%d%d%d" % (m, o, r, e)
                                        print "------"
                                        print " %d%d%d%d%d" % (m, o, n, e, y)
f()
endtime = datetime.datetime.now()
print (endtime - starttime).seconds
profile.run("f()")
