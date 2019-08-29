# def fun1(a=None,b=0,c=0,d=0):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# fun1(b=2,c=3)

# def fun2(a,b,*args):
#     print(args)
#
# fun2(1,2,3,4)
# fun2(1,2)

# def mysum(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# print(mysum(1,2,3,4))
# def fun(a,*args,b):
#     print(a)
#     print(args)
#     print(b)
#
# fun(1,2,3,4,b=5)
# fun(1,b=5)

# def fun(**kwargs):
#     print(kwargs)
#
# fun(a=10,b=20)


def fun(a,b,*args,c,d,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)







