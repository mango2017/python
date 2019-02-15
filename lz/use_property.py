# -*- coding: UTF-8 -*-
class Screen:
    @property
    def score(self):
        # print("调用了1")
        return self._score

    @score.setter
    def score(self,value):
        # print("调用了")
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Screen()
s.score = 60
print('s.score = ',s.score)