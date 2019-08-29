# 输入一段字符串 打印这个字符串中出现的字符以及字符出现的次数
# 如：ABCDABCABA
# A:4
# B:3
# C:2
# D:1

#获取用户输入
s = input('请输入内容')
#定义空字典 保存结果
dict = {}
#遍历字典
#方法一
# for ch in s:
#     #如果字符第一次出现
#     if ch not in dict:
#         #将字符加入到字典中，值为1
#         dict[ch] = 1
#     #如果不是第一次出现
#     else:
#         #查找字典中对应字符的值 加1
#         dict[ch] += 1
#方法二  休息14:27~14:40
for ch in s:
    #查找ch键在字典中的值，如果没找到默认0次
    count = dict.get(ch,0)
    #对字典ch键赋值 如果有ch键的话，次数加1
    #如果没有ch键 会向字典中添加键值对 ch:1
    dict[ch] = count+1
# 循环输出字典的每个键值对
for ch,count in dict.items():
    print(ch,'出现了',count,'次')






