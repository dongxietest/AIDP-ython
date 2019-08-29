# file: multi_inhert2.py

class A:
    def m(self):
        print("A.m")

class B:
    def m(self):
        print("B.m")

class AB(A, B):
    pass

ab = AB()
# print(AB.__bases__)
print(AB.__mro__)
ab.m()  # A.m
super(AB, ab).m()  # A.m
super(A, ab).m()  # B.m

