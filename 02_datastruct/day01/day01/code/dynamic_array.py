
# 此示例示意用动态数据来说明list内部的实现原理

class DynamicArray:
    def __init__(self):
        self.data = [None for x in range(4)]
        self.data_count = 0  # 用来记录已存储的数据的个数
        self.array_length = 4  # 能存储的数据的最大个数

    def append(self, val):
        # 在加数据之前先判断存储空间是否已满
        if self.data_count == self.array_length:
            temp = [None for _ in range(
                      self.array_length*2)]
            # 将旧数据移动新空间
            for i, x in enumerate(self.data):
                temp[i] = x
            self.array_length *= 2
            self.data = temp
        self.data[self.data_count] = val
        self.data_count += 1

    def __str__(self):
        return "DynamicArray(%s)" % self.data[:self.data_count]

    def insert(self, index, val):
        # 在加数据之前先判断存储空间是否已满
        if self.data_count == self.array_length:
            temp = [None for _ in range(
                      self.array_length*2)]
            # 将旧数据移动新空间
            for i, x in enumerate(self.data):
                temp[i] = x
            self.array_length *= 2
            self.data = temp
        # 把index提指的左侧的所有元素向右移动一个位置
        for i in range(self.data_count, index, -1):
            self.data[i] = self.data[i-1]
        # 插入数据
        self.data[index] = val
        self.data_count += 1
    def __len__(self):
        return self.data_count

    def remove(self, val):
        for i in range(self.data_count):
            if self.data[i] == val:
                # 将i之后的所有数据向前移
                for j in range(i+1, self.data_count):
                    self.data[j-1] = self.data[j]
                self.data_count -= 1

L = DynamicArray()
# L = list()
L.append(1)
L.append(3)
L.append(5)
L.append(7)
L.append(9)
print(L)  # [1, 3, 5, 7, 9]
L.insert(1, 2)
print(L)  # [1, 2, 3, 5, 7, 9]
print(len(L))  # 获取元素个数
L.remove(5)
print(L)  # [1, 2, 3, 7, 9]


L2 = list(range(100000))
import time
begin = time.time()  # 得到当前时间
# L2.insert(1, 100)
# print(L2[10001])
print('索引：', L2.index(9))
end = time.time()
print("总花费:", end-begin)





