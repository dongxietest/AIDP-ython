# 练习３：　打印当月日历
# 获取用户输入的本月第一天是星期几？5
# 获取用户输入的本月的总天数？31
# 打印本月日历。

start = int(input("输入的本月第一天是星期几？"))
days = int(input("输入的本月的总天数？"))

print("一  二  三  四  五  六  日")

# 打印开始的空白占位
print(" " * 4 * (start -1), sep="",end="")
# 当前遍历的天数
i = 1
# 当前遍历天数对应是星期几
j = start
# 外层循环遍历所有天数
while i <= days:
    # 内层循环打印周一到周日的数据
    while j < 8:
        print("%2d" % i, end="  ")
        # 当前天数内容已打印，天数加１
        i = i + 1
        # 当前天数内容已打印，星期值加１
        j = j + 1
        # 若当前行内的天数超出最大天数时，停止循环输出
        if i > days:
            break
    # 到星期日之后，换行输出
    print()
    # 重置当前的星期数，为星期１
    j = 1
# 结束输入
print()







