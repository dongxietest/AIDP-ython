# def fun(n):
#     print('进入第',n,'次递归')
#     if n==5:#递归要控制递归的层数 符合条件时终止递归的调用
#         return
#     fun(n+1)
#     print('退出第',n,'次递归')
# fun(1)

# 递归求阶乘
# 5！ = 5 * 4 * 3 * 2 * 1   5*4！
# 4! = 4 * 3 * 2 * 1       4*3！
# ...
# 1! = 1 * 1
# 0! = 1
# def fun():
#     return 5 * 4 * 3 * 2 * 1

#求n的阶乘？ n * (n-1)!
def fun(n):
    if n == 0:
        return 1
    # result = fun(n)死循环
    result = n * fun(n-1)
    return result

print(fun(5))

#排序
#L = [1,2,8,0,55,74,10,20]
#取出列表中任意一个数
#根据这个数将列表分为两部分 一部分为比这个数大的
# 一部分为比这个数小的
#跟据相同的思路对大小两个列表排序
# 当列表中的元素个数为1 或0时 返回
#拼接列表




