# 笔记
# 四年一闰，百年不闰，四百年再闰。

# 条件表达式问题：　只是表达式。
is_rui = True
year = "闰年" if is_rui == True else "平年"
#year = "闰年" if is_rui == True else year = "平年"#　错

# 标准输入语句 - 注意返回字符串类型
int(input("获取月考成绩："))
float(input("获取月考成绩："))

# 标准输出语句
# sep 参数
print(a,b,c)
# 结果：10 20 30
print(a,b,c,sep=',') #逗号分割多个变量
# 结果：10,20,30

# end　参数
print(a,b,c)
# 结果：10 20 30 （换行）
print(a,b,c,end=' ')
# 结果：10 20 30 (不换行)