
class Student:
    '''实现score只能存0~100的整数'''
    def __init__(self):
        self.__score = 0
    def set_score(self, val):
        print("set_score:", val)
        if 0 <= val <= 100:
            self.__score = val
        else:
            raise ValueError("成绩必须在0~100之间")
    def get_score(self):
        print("get_score")
        return self.__score

    score = property(get_score, set_score)

s1 = Student()
# s1.set_score(100)
# # s1.set_score(999)
# print(s1.get_score())

# 用实例属性来操作对象的成绩,无法的控制属性的取值范围
s1.score = 100
# s1.score = 999
print(s1.score)

