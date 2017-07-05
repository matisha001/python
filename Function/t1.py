# -*- coding: UTF-8 -*-

# 定义函数
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;
 
# 调用函数
printme("调用函数");


# 值传递
def ChangeInt( a ):
    a = 10
    print a # 结果是 10
b = 2
ChangeInt(b)
print b # 结果是 2

# 对象传递


# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "mylist函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30];
print "mylist原始值:", mylist
changeme( mylist );
print "mylist函数外取值: ", mylist


# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print "函数内 : ", total
   return total;
 
# 调用sum函数
total = sum( 10, 20 );