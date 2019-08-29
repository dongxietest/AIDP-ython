# 此示例示意能提供迭代器的可迭代对象的实现原理

class MyRange:
    '''此示例示意把MyRange做成可迭代对象来提供数据'''
    def __init__(self, start,
                 stop = None,
                 step=None):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        # 判断第三个参数
        if step is None:
            self.step = 1
        else:
            self.step = step

    def __iter__(self):
        '''此方法要求必须返回一个迭代器'''
        print("__iter__方法被调用!")
        return MyRangeIter(self)

class MyRangeIter:
    def __init__(self, iterable):
        self.beg = iterable.start
        self.end = iterable.stop
        self.step = iterable.step

    def __next__(self):
        if self.beg >= self.end:
            raise StopIteration
        r = self.beg
        self.beg += self.step
        return r

# myiterable = MyRange(10)
# it = iter(myiterable)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break

for x in MyRange(1, 10, 3):
    print(x)


# myr = MyRange(1, 10, 2)
# with MyRange(1, 10, 2) as myr:
#     print("hello")





