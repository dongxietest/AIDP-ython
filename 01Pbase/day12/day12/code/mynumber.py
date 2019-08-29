# file: mynumber.py


class MyNumber:
    def __init__(self, v=0):
        self.data = v

    def __str__(self):
        return "数字:%s" % self.data

    def __repr__(self):
        return "MyNumber(%d)" % self.data

n1 = MyNumber(100)
# print(n1)
# print(str(n1))
# print(n1.__str__())
print(repr(n1))
print(n1.__repr__())
n2 = MyNumber(200)
print(repr(n2))  # "MyNumber(100)"



