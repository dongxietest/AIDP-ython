

try:
    try:
        a = 100
        999 / 0  # 出错
        print(a)
    finally:
        print("finally 子句被调用!!!")
except:
    print("程序出现了错误，但已经被捕获,程序已转为正常状态")

print("程序正常退出")