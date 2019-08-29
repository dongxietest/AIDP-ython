

def fn(a, b):
    '''要求a是0~100之间的数,
    此函数返回a/b的值'''
    if a > 100:
        e =  ValueError(str(a) + "大于100错误")
        raise e
    elif a < 0:
        raise ValueError(str(a) + '小于0错误')
    if b == 0:
        raise ZeroDivisionError('b为零')

try:
    fn(-100, 0)
except ValueError as err:
    print("fn内已出错，抛出异常,第一个参数不在0~100之间")
    print('err=', err)
except ZeroDivisionError:
    print("第二个参数传为0了")

print("程序正常退出")