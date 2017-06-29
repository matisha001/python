# -*- coding: UTF-8 -*-

count = 0
while (count < 1):
   print 'The count is:', count
   count = count + 1
else :
   print "Good bye!"

# var = 1
var = 2
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num


fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print fruit

import math
print math.pi