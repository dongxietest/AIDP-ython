class Human(object):
    def __init__(self, n, a):
        self.__name = n  # 姓名
        self.age = a  # 年龄

    def infos(self):
        print("姓名:", self.__name)
        print("年龄:", self.age)

class Student(Human):
    def __init__(self, n, a, score):
        super().__init__(n, a)
        self.score = score
    def infos(self):
        super(Student, self).infos()
        print("成绩:", self.score)

h1 = Student("小张", 18, 0)
h1.infos()
# h1.__name = 'XXX'  # 让此做法无效
print(h1.__name)  # 报错
h1.infos()


