# -*- coding: UTF-8 -*-
import time;  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks


localtime = time.localtime(time.time())
print "本地时间为 :", localtime

localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 


print  time.localtime()


print "%d" % time.altzone


print time.clock()


print "%s" % time.ctime()

print "%s" % time.gmtime()


print "time.localtime() : %s" % time.localtime()