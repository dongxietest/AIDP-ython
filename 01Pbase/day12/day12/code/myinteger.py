# file: myinteger.py


class MyInteger:
    def __init__(self, v=0):
        self.data = v

    def __str__(self):
        return "整数: %d" % self.data

    def __add__(self, other):
        return MyInteger(self.data + other.data)

    def __sub__(self, other):
        return MyInteger(self.data - other.data)
    def __and__(self, other):
        return MyInteger(self.data*2-other.data)

n1 = MyInteger(500)
n2 = MyInteger(200)
n3 = n1 + n2  # 等同于 n3 = n1.__add__(n2)
print(n3)  # 整数300
n4 = n1 - n2
print(n4)
n5 = n1 & n2  # n1.__and__(n2)
print(n5)


