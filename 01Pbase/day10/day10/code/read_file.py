

try:
    # myf = open('myfile.txt')  # 以只读方式打开文件'myfile.txt'
                # 如果是相对路径,是相对于主程序的启动路径
    myf = open('/home/tarena/waid1905/day10/code/myfile.txt')  # 以只读方式打开文件'myfile.txt'

    # myf = open('aaaaaaaaaaaa.txt')  # 以只读方式打开文件'myfile.txt'
    # 读/写操作
    s = myf.read()  # 此时s = 'ABC\n123\nhello!'
    print("文件中有%d个字符" % len(s))
    print("s =", s)
    myf.close()  # 关闭文件
except OSError:
    print('打开文件失败!!!')
