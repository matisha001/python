#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

a = 21
b = 10

 
c = a + b
print "1 - c :", c
 
c = a - b
print "2 - c :", c 
 
c = a * b
print "3 - c :", c 
 
c = a / b
print "4 - c :", c 
 
c = a % b
print "5 - c :", c
 
# 修改变量 a 、b 、c

c = a**b 
print "6 - c :", c
 

c = a//b 
print "7 - c :", c


list = [1, 2, 3, 4, 5 ,21 ];
 
if ( a in list ):
   print "a in";
   print '21111111111111'
else:
   print "a not in"
# a=10 
if ( a is b ):
   print "sssssssssssss1"

else:
   print "eeeeeeeeeee2"
num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine