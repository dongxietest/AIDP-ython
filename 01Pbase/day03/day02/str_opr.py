# 字符串操作
# １. 运算符操作
# +  *  +=  *=
str1 = "Windows"
str2 = "Ubuntu"
print(str1 + str2) # WindowsUbuntu

# 只能和整数相乘，不能使用浮点数
str3 = str1 * 3
str4 = str1 + str1 + str1
print(str3, str4) # 都是WindowsWindowsWindows


print("before:", str1, str2)
str1 += str2
print("after:", str1, str2)


print("before:", str2)
str2 *= 2
print("after:", str2)

# > < == >= <= !=
str3 = "a"
str4 = "A"
print(str3 < str4)

# ascii编码的使用
# 八进制：　　077
# 十六进制：　3F
# 字符：　　　?
print("?")
print("\077")
print("\x3F")
print("\u003F")
print("\U0000003F")

# 练习：使用上面的方式打印“$”符号
# 八进制表示：　044
# 十六进制表示：　24
print("\044")
print("\x24")
print("\u0024")
print("\U00000024")


str5 = "PythonBase"
print(len(str5))
print(len("PythonBase"))

# 小测试１：
# 写出如下代码的输出结果：
# print(len("sae//\\123\07789890\u4578"))
print(len("sae//\\123\077\x89890\u4578")) # 15

# 小测试２：
# 写出如下代码的输出结果：
print(len(r"sae//\\123\077\x89890\u4578"))

# 索引操作
# 字符串[正向索引／反向索引下标值]
mail = "mail4homework@yeah.net"
print(len(mail))
# 正向索引下标： 0  －＞  21
# 反向索引下标：-1 －>　-22
# 输出第四个字符
# 正向第Ｎ个字符：对应下标N-1
# 反向第Ｎ个字符：对应下标-len+(N-1)
print(mail[3], mail[-19])
# 中间字符：(取第１１个字符）
index = int(len(mail)/2) # 11
num = len(mail)
print(index)

print(mail[index-1]) # 下标值对应１０
print(mail[-num+(index-1)])# 下标值对应－２２＋１０＝－１２


# 切片
# 字符串[ 起始索引 : 结束索引 : 　步长  ]
# 步长，可以省略，默认值为１
print(mail[0:4])
print(mail[0:4:2])
# 当反向切片取到首元素前一位时，结束索引处不用填写使用默认值即可
print(mail[3: :-1]) # 取liam


# 练习：　取数据：ten.haey@krowemoh4liam
# 即：反向取全部内容(逆序)
# 反向：起始索引默认从最后一个元素开始
# 反向：结束索引默认到首元素的下一位置
print(mail[::-1])
print(mail[21::-1])# 使用正向索引的最后一个下标值
print(mail[-1::-1])# 使用反向索引的最后一个下标值


# 练习：　取数据：“mail4homework@yeah.net"
print(mail[:])
print(mail[::1])
print(mail[0:])
print(mail[0:22])
print(mail[0:22:1])

# 小测试
print(mail[21:-23:-1])
print(mail[-1:-23:-1])

# 其他序列函数
print(max(mail))
print(min(mail))