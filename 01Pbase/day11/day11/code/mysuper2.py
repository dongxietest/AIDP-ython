class A:
    def m(self):
        print('A')

class B(A):
    def m(self):
        print("B")

class C(B):
    def m(self):
        print("C")
        super().m()
        super(B, self).m()  # A

c = C()
c.m()
