
# L = [2, 3, 5, 7]
L = "ABCD"

# 方法1
for x in L:
    print(x)

# 方法2:
it = iter(L)  # 让L提供迭代器
while True:
    try:
        x = next(it)  # 从迭代器中取值
        print(x)
    except StopIteration:
        break

