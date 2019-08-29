#获取可迭代对象中的所有的奇数放入列表中
def isodd(x):
    return x % 2 == 1

# L = []
# for x in filter(isodd,range(1,10)):
#     L.append(x)
#
# print(L)
print(list(filter(isodd,range(1,10))))
print([x for x in filter(isodd,range(1,10))])