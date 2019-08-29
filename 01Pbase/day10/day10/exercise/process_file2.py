

fr = open('myfile1.txt', 'rb')  # t-->text, b-->binary
b = fr.read()  # b = b'xxxxx'
fr.close()

# s = b.decode()
fw = open('myfile2.txt', 'wb')  # b-->binary
fw.write('====== 文件开始 ======\n'.encode())
fw.write(b)
# if b[-1] != b'\n':
if b[-1] != 0x0a:
    fw.write(b'\n')
fw.write('====== 文件结束 ======\n'.encode())
# 此外故意没有关闭文件
fw.close()



