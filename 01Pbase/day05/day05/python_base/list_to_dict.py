# 已知有两个等长列表L1和L2,生成相应的字典
# L1 = [1001,1002,1003,1004]
# L2 = ['Tom','Jerry','Alice','Bob']
# 生成的字典为
# {'Tom':1001,....}
L1 = [1001,1002,1003,1004]
#     0    1    2     3
L2 = ['Tom','Jerry','Alice','Bob']
#方法一
# dict = {L2[i]:L1[i] for i in range(len(L1))}
#方法二
dict = {k:L1[L2.index(k)] for k in L2}
print(dict)
