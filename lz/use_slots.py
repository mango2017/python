# -*- coding: UTF-8 -*-
class Student:
    __slots__ = ('name','age')

class GraduateStudent(Student):
    __slots__ = ('score')
    pass

s = Student() #创建新的实例
s.name = 'Michael' #绑定属性name
s.age = 25 #绑定属性age
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError',e)

g = GraduateStudent()
g.score = 99
print('g.score = ',g.score)

g.name = '111'
print(g.name)
g.aa = "aaa"
