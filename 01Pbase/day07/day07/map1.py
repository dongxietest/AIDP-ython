# 求1～9的平方的和
print('方法一')
s = 0
for i in range(1,10):
    s += i ** 2
print(s)
print('方法二')
s = 0
def mypow(x):
    return x**2
for x in map(mypow,range(1,10)):
    s += x
print(s)
print('方法三')
s = 0
for x in map(lambda x:x**2,range(1,10)):
    s += x
print(s)
print('方法四')
print(sum(map(lambda x:x**2,range(1,10))))