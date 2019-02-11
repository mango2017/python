# -*- coding: UTF-8 -*-

import time as t

class Mytimer():
    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.prompt = "未开始计时！"  #提示语
        self.lasted = []  #结束时间和开始时间的查 6个数
        self.begin = 0  #开始时间
        self.end = 0  #结束时间

    def __str__(self):
        return self.prompt

    __repr__ = __str__


    #计算定时器之和
    def __add__(self, other):
        prompt = "一共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    #开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()停止计时！"
        print("计时开始...")

    #停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()进行计时！")
        self.end = t.localtime()
        self._calc()
        print("计时结束！")

    #内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        self.begin = 0
        self.end  = 0

        # print(self.prompt)

t1 = Mytimer()
t1.start()
t.sleep(5)
t1.stop()
print t1

t2 = Mytimer()
t2.start()
t.sleep(2)
t2.stop()
print t2
print t1+t2


