
def f1():
    s = "错误信息"
    e = ValueError(s)
    raise e  # 抛出对象
    # raise ValueError  # 抛出类

def f2():
    try:
        f1()
    except ValueError as aaa:
        print("f2收到了f1传来的", aaa)
        raise

def f3():
    f2()

# 我今天在此处得到错误信息s
try:
    f3()
except ValueError as err:
    print("f3的调用收到错误信息")
    print(err)





# def f1():
#     s = "错误信息"
#     return s
#
# def f2():
#     r = f1()
#     return r
#
# def f3():
#     r = f2()
#     return r
#
# # 我今天在此处得到错误信息s
# r = f3()
# print(r)
#


print("程序正常退出")