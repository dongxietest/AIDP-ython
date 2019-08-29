# file: multi_inherit.py

class A:
    def ma(self):
        print("A.ma方法被调用")

class B:
    def mb(self):
        print("B.mb方法被调用")

class AB(A, B):
    pass

ab = AB()  #创建实例对象
ab.ma()
ab.mb()
ab.__init__()  # 继承自object类

