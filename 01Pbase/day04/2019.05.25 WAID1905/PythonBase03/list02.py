"""
    列表的高级操作
"""

# # 深拷贝与浅拷贝
# L01 = ["xiaoli zhang", "xiaoyue su"]
# L02 = L01
# L01[0] = "xiaoli su" # 更改了Ｌ01关联对象的内容
# print(L02[0])
#
# L01 = ["xiaoli zhang", "xiaoyue su"]
# L02 = L01
# L01 = ["xiaoli su"] # 更改了L01关联的对象
# print(L02[0])
#
# L01 = ["xiaoshan zhou", "xiallan gong"]
# L02 = L01[:] # 创建副本
# L01[0] = "xiaoshan su" # 更改了Ｌ01关联对象的内容，不影响副本
# print(L02[0])
#
# L01 = [500] # 更改了Ｌ０１关联的对象，　也不影响副本
# print(L02[0])
#
#
#
# L01 = ["xiaoshan zhou", ["xiaolan gong", 28]]
# L02 = L01
# L01[1][0] = "xiaoli su" # 更改了Ｌ01关联对象的内容, L02也关联此对象
# print(L02[1][0])
#
#
# L01 = ["xiaoshan zhou", ["xiaolan gong", 28]]
# L02 = L01[:] # 切片副本
# L01[1][0] = "xiaoli su" # 浅拷贝，只复制一层，对于内部嵌套列表的内容不做复制
# print(L02[1][0])
#
#
# L01 = ["xiaoshan zhou", ["xiaolan gong", 28]]
# L02 = L01.copy() # 列表方法copy,备份数据
# L01[1][0] = "xiaoli su" # 浅拷贝，只复制一层，对于内部嵌套列表的内容不做复制
# print(L02[1][0])
#
#
# # 如何实现深拷贝
# import copy
#
# L01 = ["xiaoshan zhou", ["xiaolan gong", 28]]
# L02 = copy.deepcopy(L01)
# L01[1][0] = "xiaoli su" # 深拷贝
# print(L02[1][0])


# 对比字符串和列表
#           字符串                 列表
# 是否为序列    Ｖ                　Ｖ
# 存储内容　　每个元素都是单个字符      每个元素可以存放任意类型数据
# 是否可变　　　不可变                可变
# 是否可迭代　　Ｖ　　　　　　　　　　　　Ｖ
# 相互转换？

# 如何将列表转换成字符串：
L03 = ["file", "edit", "view"]
# 使用的语法：   “列表元素分割字符”.join(列表变量)
S01 = "#".join(L03)
print(S01)

# 如何将字符串转换成列表：
# 使用语法：　　字符串变量.split("分割字符串的字符")
L04 = S01.split("#")
print(L04)











