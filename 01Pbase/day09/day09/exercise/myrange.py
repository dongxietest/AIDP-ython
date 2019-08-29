def myrange(start, stop=None, step=None):
    # 校正开始的结束两个参数
    if stop is None:
       stop = start
       start = 0
    if step is None:  # 当第三个参数没有给出时，步长默认为1
        step = 1
    i = start  # 从start开始生成
    while i < stop:  # 当stop结束，不包含stop
        yield i  # 生成i 送回给调用者
        i += step  # 在下次取数时，将i增加step步长


for x in myrange(3):
    print(x)  # 打印 0, 1, 2
print('====================')
for x in myrange(5, 8):
    print(x)  # 打印 5, 6, 7
print('====================')
for x in myrange(5, 10, 2):
    print(x)   # 打印 5, 7, 9