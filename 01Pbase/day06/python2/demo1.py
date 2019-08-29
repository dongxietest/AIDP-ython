print('demo1开始执行')
def mymax(a,b):
    '''
    求a和b两个数字的最大值
    参数:param 函数的使用者传递给函数定义者的信息
    返回值:return 函数定义者传递给函数使用者的结果
    :param a:数字
    :param b:数字
    :return:None
    '''
    print('mymax执行了')
    if a > b:
        return a
    else:
        return b
    # return None
    print('mymax结束了')

a = 10
b = 20
print(max(a,b))
print(mymax(a,b))
# a = 20
# b = 15
# mymax(a,b)