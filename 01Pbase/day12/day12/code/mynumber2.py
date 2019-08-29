# file: mynumber2.py
# 此示例示意反向算术运算符重载


class MyNumber:
    def __init__(self, v=0):
        self.data = v

    def __str__(self):
        return "数字:%s" % self.data

    def __mul__(self, other):
        return MyNumber(self.data * other)
    def __rmul__(self, other):
        return MyNumber(self.data *  other)
    def __rsub__(self, other):
        return MyNumber(other-self.data)
n1 = MyNumber(100)
# n2 = n1 * 2   # n1.__mul__(2)
n2 = 2 * n1  # n1.__rmul__(2)  # reverse
print(n2)  # 数字: 200
n3 = 2 - n1  # n1.__rsub__(2)  结果 -98
print(n3)


