# 练习：
# 定义函数 判断列表中是否存在相同的元素
# list = [1,2,1,3,5,7]
# for r in range(0,len(list)-1):
#     for c in range(r+1,len(list)):
#         if list[r] == list[c]:
#             print('存在相同元素')
#             break
# print('没有相同元素')
def is_repeating(list):
    for r in range(0,len(list)-1):
        for c in range(r+1,len(list)):
            if list[r] == list[c]:
                return True
    return False

list = [1,2,1,3,5,7]
print(is_repeating(list))






