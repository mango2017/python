# -*- coding: UTF-8 -*-

#abs() 函数返回数字的绝对值
print "abs(-45) : ",abs(-45)
print "abs(100.12) : ",abs(100.12)
print "abs(119L) : ",abs(119L)

# divmod()函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组
print divmod(7,2)
print divmod(8,2)
print divmod(1+2j,1+0.5j)  #这个是咋计算的呀

# str() 函数将对象转化为适于人阅读的形式
s = 'RUNOOB'
print str(s)
dict = {'a','b','c'}
print str(dict)

# range() 函数可创建一个整数列表，一般用在 for 循环中
print range(10)     # 从 0 开始到 10
print range(1,11)   # 从 1 开始到 11
print range(0,30,5) # 步长为 5
print range(0)

x = 'runoob'
for i in range(len(x)):
    print(x[i])