# file: mywith.py

# 此示例示意让自定义的类能实现用with语句进行管理
class A:
    def __init__(self):
        print('打开的电脑的USB外部设备')

    def sayHello(self):
        print("你好哦!")
    def free(self):
        print("关闭USB外部设备")

    def __enter__(self):
        print("进入with语句")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.free()
        print("已离开with语句")

with A() as a:   # a = A()
    a.sayHello()
    x = int("ABCD")
    # ValueError: xxxxxxxx


# a = A()
# a.sayHello()
# 3 / 0
# a.free()
