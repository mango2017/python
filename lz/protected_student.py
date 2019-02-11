# -*- coding: UTF-8 -*-

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson',59)
print('bart.get_name() = ',bart.get_name())
bart.set_score(60)
print('bart.get_score() = ',bart.get_score())
print('bart.score = ',bart._Student__score)

#外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量
bart.__name = "xxx"
print bart.__name
print('bart.get_name() = ',bart.get_name())

print('do not use bart._Student__name:',bart._Student__name)