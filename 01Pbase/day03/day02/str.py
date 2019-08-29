# int float 不能存放用户姓名
# 使用str　字符串类型

# 存放内容：　张小黎
str = '张小黎'
str1 = "张小黎"
str2 = '''张小黎'''
str3 = """张小黎"""
print(str, str1, str2, str3)

# 存放内容：　I'm Amy.
str4 = "I'm Amy."
str5 = '''I'm Amy.'''
str6 = """I'm Amy."""
print(str4,str5, str6)

# 存放内容： 我的名字是"张小黎".
str7 = '我的名字是"张小黎".'
str8 = '''我的名字是"张小黎".'''
str9 = """我的名字是"张小黎"."""
print(str7, str8, str9)

# 存放内容：　I'm xiaoli Zhang. 我的名字是"张小黎".
str10 = '''I'm xiaoli Zhang. 我的名字是"张小黎".'''
str11 = """I'm xiaoli Zhang. 我的名字是"张小黎"."""
print(str10, str11)

# 存放内容：　字符串可使用三个单引号(''')括起来.
str12 = """字符串可使用三个单引号(''')括起来."""
str13 = "字符串可使用三个单引号(''')括起来."
# str14 = '字符串可使用三个单引号(''')括起来.' # 错
print(str12, str13)

# 存放内容：　字符串可使用三个双引号(""")括起来.
str14 = '''字符串可使用三个双引号(""")括起来.'''
str15 = '字符串可使用三个双引号(""")括起来.'
print(str14, str15)

# 存放内容：　
# I'm xiaoli Zhang. 我的名字是"张小黎".字符串可使用三个单引号(''')或者双引号(""")括起来.
# Python字面值的隐式拼接
str16 = '''I'm xiaoli Zhang. 我的名字是"张小黎".'''    "字符串可使用三个单引号(''')"    '或者双引号(""")括起来.'
# 使用转义字符
str17 = 'I\'m xiaoli Zhang. 我的名字是"张小黎".字符串可使用三个单引号(\'\'\')或者双引号(""")括起来.'
str18 = "I'm xiaoli Zhang. 我的名字是\"张小黎\".字符串可使用三个单引号(''')或者双引号(\"\"\")括起来."
print(str16, str17, str18)

# 存放内容：　C:\Users\Python\Desktop\MongoDB\MongoDB_1.TXT
# str19 = "C:\Users\Python\Desktop\MongoDB\MongoDB_1.TXT" # 报错truncated \UXXXXXXXX escape
# 使用转义字符表示
str19 = "C:\\Users\\Python\\Desktop\\MongoDB\\MongoDB_1.TXT"
# 使用原始字符串的内容　－　raw字符串
str20 = r"C:\Users\Python\Desktop\MongoDB\MongoDB_1.TXT"
str21 = r'C:\Users\Python\Desktop\MongoDB\MongoDB_1.TXT'
str22 = r'''C:\Users\Python\Desktop\MongoDB\MongoDB_1.TXT'''
str23 = r"""C:\Users\Python\Desktop\MongoDB\MongoDB_1.TXT"""
print(str19, str20, str21, str22, str23)







