# a = 100#全局变量

# def wai_fun():
#     a = 10#对于wai_fun来说 是局部变量
#           #对于nei_fun来说 是外部嵌套函数变量
#     def nei_fun():
#         a = 1#是nei_fun的局部变量
#         print(a)
#     nei_fun()
#     print(a)
#
# wai_fun()
# print(a)
# a = 100
# def g_fun(a):
#     # a = 10
#     global a#报错 不能先声明局部变量再声明为全局变量
#     # a = 20
#     print(a)
#
# g_fun(10)
# print(a)#10
def wai_fun():
    a = 10#对于wai_fun来说 是局部变量
          #对于nei_fun来说 是外部嵌套函数变量
    # a = 1
    def nei_fun():
        nonlocal a
        a = 1
        print(a)
    nei_fun(20)
    print(a)

wai_fun()





