

fr = open('myfile1.txt', 'rt')  # t-->text, b-->binary
s = fr.read()  # b = b'xxxxx', s = b.decode()
fr.close()

fw = open('myfile2.txt', 'w')
fw.write('====== 文件开始 ======\n')
fw.write(s)
if s[-1] != '\n':
    fw.write('\n')
fw.write('====== 文件结束 ======\n')
# 此外故意没有关闭文件
fw.flush()  # 强制进行IO操作
# fw.close()
while True:
    pass



