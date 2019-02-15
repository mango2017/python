# -*- coding: UTF-8 -*-
class Student:
    __slots__ = ('name','age')  #用tuple定义允许绑定的属性名称

s = Student()
s.name = 'jly'
print(s.name)
s.age = 25
print(s.age)
s.score = 100
print(s.score)

class GranuateStudent(Student):
    pass

g = GranuateStudent()
g.score = 101
print(g.score)