# -*- coding: UTF-8 -*-

#集合的创建与添加
a = {1,2,3}
print(a)
a.add(9)
print(a)

aa = {1,3,'sxt'}
bb = {'he','it','sxt'}
print(aa.union(bb))  #并集
print(aa.intersection(bb)) #交集
print(aa.difference(bb)) #差集