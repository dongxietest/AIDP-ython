

f = open('aaa.csv', 'rb')
while True:
    line = f.readline()  # line绑定字节串
    if not line:  # line为空时停止读取
        break
    # print(line)
    s = line.decode('gbk')
    print(s)
f.close()