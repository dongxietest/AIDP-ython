class A:
    def m(self):
        print('A')

class B(A):
    def m(self):
        print("B")

class C(B):
    def m(self):
        print("C")

c = C()
c.m()  # C
super(C, c).m()  # B
super(B, c).m()  # A

