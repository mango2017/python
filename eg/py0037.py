# -*- coding: UTF-8 -*-

r1={"name":"高小一","age":18,"salary":30000,"city":"北京"}
r2={"name":"高小二","age":19,"salary":20000,"city":"上海"}
r3={"name":"高小五","age":20,"salary":10000,"city":"深圳"}

tb = [r1,r2,r3]
print(tb)

print(tb[1].get('salary'))

for i in range(len(tb)):
    print(tb[i].get('salary'),tb[i].get('age'))
