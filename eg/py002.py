# -*- coding: UTF-8 -*-
def MyFisrtFunction():
    print("这是我创建的第一个函数")
    print("我表示很激动....")
    print("哈哈哈哈")


MyFisrtFunction()
MyFisrtFunction()

def MySecondFunction(name):
    print(name+"呵呵")

MySecondFunction("啦啦")


def MyThirdFunction(num1,num2):
    return num1+num2

total = MyThirdFunction(2,3)
print(total)


def MyFourFunction(name,word):
    print(name+ "->" +word)

MyFourFunction(word="aaa",name="28")

# def test(*params):
#     print("参数长度是",len(params))
#
#
# test(1,2,3,3)



def test(*params, **exps):
    print("参数长度是",len(params),exps)


test(1,2,3,4,exps=8)




