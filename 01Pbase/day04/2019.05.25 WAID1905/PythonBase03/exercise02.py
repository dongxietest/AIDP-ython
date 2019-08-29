# 练习１：　累加开始值到结束值之间所有个位数不为2 3 5 7 9的整数。
# １　获取开始数据（包含）
# ２　获取结束数据（不包含）
# ３　打印筛选后的总和：
begin = int(input("请输入开始的数据（包含):"))
end = int(input("请输入结束的数据（不包含）："))

# 计算累加的结果
sum_value = 0

# 遍历所有的数据
for i in range(begin, end):
    # 个位数
    unit = i % 10
    if unit == 2 or \
        unit == 3 or \
        unit == 5 or \
        unit == 7 or \
        unit == 9:
        continue
    sum_value += i

print("在区间[%d,%d)内，个位数不为2 3 5 7 9的数据之和为:%d" % (begin, end, sum_value))

