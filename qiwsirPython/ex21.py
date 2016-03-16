#!/usr/bin/env python
#coding:utf-8
#Created by Jeff on 2016/3/13 22:15
# 21、美国体育作家Bill James发明了一种算法，通过该算法能够知道在NBA比赛中，领先对手多少分是“安全的”，即能够确保最终赢得比赛。他的算法如下：
# 获取领先一队的分数
# 减去三分
# 如果目前领先队控球，那么加上0.5分；如果是落后队控球，减去0.5分（数字小于零则变成零）
# 计算平方后的结果。
# 如果结果比当前比赛剩下的时间秒数大，那么这个领先是安全的。
# 请认真阅读上述算法，并将它转化为Python程序。当用户输入领先一队的分数和比赛时间、某队当前是否控球后，即可反馈用户，该队是否“安全”领先。

def isSafe(score, time, possession):
    #减去三分
    safeScore = score - 3
    #球权
    if possession == 'y':
        safeScore += 0.5
    else:
        safeScore -= 0.5
        if safeScore < 0:
            safeScore = 0
    safeScore  = safeScore ** 2
    if safeScore > time:
        return "安全"
    else:
        return "不安全"
if __name__ == "__main__":
    score = int(raw_input("请输入领先队分数："))
    time = float(raw_input("请输入剩余比赛时间(秒)："))
    possession = raw_input("请输入领先队是否控球(Y/N)：").lower()
    print "领先队",isSafe(score, time, possession)