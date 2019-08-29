import os
import math
import time

import numpy

import mymod

class Student:
    '''实现score只能存0~100的整数'''
    def __init__(self):
        self.__score = 0

    @property
    def score(self):
        '''getter'''
        print("get_score...")
        return self.__score

    @score.setter
    def score(self, val):
        print("set_score:", val)
        if 0 <= val <= 100:
            self.__score = val
        else:
            raise ValueError("成绩必须在0~100之间")

s1 = Student()
# 用实例属性来操作对象的成绩,无法的控制属性的取值范围
s1.score = 100
# s1.score = 999  # 调用s1.set_score(999)
print(s1.score)  # 调用s1.get_score()

