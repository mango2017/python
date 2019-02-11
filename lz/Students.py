# -*- coding: UTF-8 -*-

class Students(object):
    name = "students"

s = Students()
print(s.name)
print(Students.name)
s.name = "Michael"
print(s.name)
print(Students.name)
del s.name
print(s.name)