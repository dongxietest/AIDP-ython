# myadd = lambda x,y : x+y
# print(myadd(10,20))
# (lambda x,y : x + y)(10,20)

#判断x的平方+1能否被3整除 如果能True
# def fun(x):
#     # if (x**2+1) % 3 == 0:
#     #     return True
#     # else:
#     #     return False
#     return (x**2+1) % 3 == 0
# fun = lambda x:(x**2+1) % 3 == 0
# print(fun(10))
# print(fun(12))

# def get_fun(op):
#     #{'+':myadd,'-':mysub,...}
#     if op == '+':
#         return lambda x,y:x + y
#     elif op == '-':
#         return lambda x,y:x - y
#     elif op == '*':
#         return lambda x,y:x * y
#     elif op == '/':
#         return lambda x,y:x / y