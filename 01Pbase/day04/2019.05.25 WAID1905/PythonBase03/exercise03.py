# 练习２：　一张纸的厚度是0.01毫米，问计算对折多少次，厚度能超过珠穆郎玛峰8844.43米。
# 纸张厚度　单位米
tickness = 0.01 / 1000
# 折叠次数
count = 0
# while循环实现
while tickness < 8844.43:
    # 厚度翻倍
    tickness *= 2 # tickness = tickness * 2
    # 折叠计数加１
    count += 1    # count = count + 1
    print("第%d次折叠厚度%f." % (count, tickness))

print("当一张纸折叠" + str(count) + "次时，超过珠穆郎玛峰8844.43米。")










