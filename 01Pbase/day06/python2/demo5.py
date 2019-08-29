# a = 100#全局变量 在模块内的所有代码都可以直接访问
# b = '20'
# name = 'shibw'
# print(a)
# def fun():
#     a = 10
#     age = 18
#     address = '北京'
#     # a = 10#局部变量 函数内使用函数调用时创建 函数结束时自动销毁
#     print(locals())
#
# fun()
# print(globals())
# L = [1,2,3]
# def fun(list):
#     L = list#创建了一个局部变量 值为形参的值
#     print(L)
#
# fun([4,5,6])
# print(L)
# def fun2(list):
#     L += list#出错 不可以在局部直接操作全局变量
    # L = L + list

# fun2([4,5,6])
L = [1,2,3]
def fun3(list):
    L.extend(list)#操作原列表，向列表中添加值
    #列表还是那个列表 值发生改变

fun3([4,5,6])
print(L)












