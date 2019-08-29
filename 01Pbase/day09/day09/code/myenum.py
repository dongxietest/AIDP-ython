# file : myenum.py


def myenumerate(iterable, start=0):
    for x in iterable:
        yield (start, x)
        start += 1

# 方法2
names = ["中国移动", "中国电信", "中国联通"]
for i, x in myenumerate(names, 1):
    print("第", i, '个是:', x)

