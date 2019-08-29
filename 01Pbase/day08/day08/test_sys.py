import sys

# print(sys.path)
# print(sys.version)
# print(sys.version_info)
# print(sys.platform)

# print(sys.argv)#命令行参数列表 第一个值为当前模块的路径
# print(sys.argv[1])#第一个命令行位置参数
# print(sys.argv[2])

def fun():
    print('fun正在运行')
    sys.exit()
    print('fun运行结束')

fun()
print('程序结束')









