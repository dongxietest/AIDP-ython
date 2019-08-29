# file: mynumber2.py
# 此示例示意反向算术运算符重载


class MyNumber:
    def __init__(self, v=0):
        self.data = v

    def __str__(self):
        return "数字:%s" % self.data

    def __add__(self, other):
        print("__add__")
        return MyNumber(self.data + other)

    # def __iadd__(self, other):
    #     self.data += other
    #     return self


n1 = MyNumber(100)
# n1 = n1 + 2
n1 += 2  # n1 = n1 + 2
print(n1)  # 102

