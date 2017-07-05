# -*- coding: UTF-8 -*-

# 定义函数
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;


# 必备参数
printme('2')


# 关键字参数
printme( str = "My string");



#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;

printinfo( name="miki" );


# 不定长参数
# 可写函数说明
def printinfo1( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return;
 
# 调用printinfo 函数
printinfo1( 10 );
printinfo1( 70, 60, 50 );