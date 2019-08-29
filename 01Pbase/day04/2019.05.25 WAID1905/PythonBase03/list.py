"""
    列表
"""

# 基本操作
# 创建　－　字面值
list01 = []
list02 = [100, 3.14, "abc", None, True, 5+6j]
# 创建　－　构造函数
list03 = list()
list04 = list("hello,world!")
print(list01, list02, list03, list04, sep='\n')

# 增加元素
# 尾部追加语法：　列表变量名.append(添加的数据)
list02.append("append")
# 指定位置添加语法：列表变量名.insert(添加数据对应的索引下标值, 添加的数据)
list04.insert(1, "o")
print(list02, list04, sep='\n')

# 删除元素
# 根据元素删除数据：列表变量名.remove(要删除的数据)
list04.remove('e')
print(list04)
# 根据位置删除数据：del  列表变量名[要删除数据对应的下标值]
del list02[5]
print(list02)
# 根据切片删除数据：del  列表变量名[起始下标值:终止数据下一位置的下标值:步长]
del list04[0:5:1]
print(list04)

# 获取元素
# 索引获取数据：列表变量名[要获取数据对应的下标值]
print(list02[1])
# 切片获取数据：列表变量名[起始下标值:终止数据下一位置的下标值:步长]
print(list04[1:6:1])

# 更改指定元素的值
# 索引获取数据：列表变量名[要获取数据对应的下标值]
print(list02[1])
list02[1] = 3.1415926
print(list02[1])

# 切片获取数据：列表变量名[起始下标值:终止数据下一位置的下标值:步长]
print(list04[1:6:1])
list04[1:6:1] = ['d', 'l', 'r', 'o', 'w']
print(list04[1:6:1])

# 遍历列表
# 正向遍历
# 切片副本
for item in list02[:]:
    print(item, end="  ")
print()

# 索引下标
for i in range(len(list02)):
    print(list02[i], end="  ")
print()

# 逆向遍历
# 切片副本
for item in list02[::-1]:
    print(item, end="  ")
print()

# 索引下标
# -1 -2 -3 -len (-len-1)
for i in range(-1, -len(list02)-1, -1):
    print(list02[i], end="  ")
print()

# 列表的嵌套
# 字面值
list05 = [1, 10, 100, [2, 20, 200], [3, 30, 300]]
print(list05)
# 变量
list06 = [list02, list04]
print(list06)

# 列表的常用函数
print(list02.index(100))
# insert/count/remove/copy/append/extend/clear/sort/reverse/pop


# 通用操作
# 运算符
# + 拼接
# += 拼接并重新关联
list07 = list02 + list04
print(list07)
list02 += list04 # list02 = list02 + list04
print(list02)

# * 重复
# *= 重复并重新关联
list08 = [1,2,3]
list09 = [3,4,5]
list08 = list08 * 3
print(list08)
list09 *= 5
print(list09)

# 比较运算
# <  <=  > >= == !=
print(list08 > list09)


# 成员运算
# in / not in
print(3 in list08)
print(10 not in list09)


# 索引操作

# 切片操作

# 内键函数

print(len(list08))
print(max(list08))
print(min(list08))
print(any(list08))
print(all(list08))

