'''
自定义模块
hi：普通文本
psrat:函数
'''
hi = 'hello world'

def pstar(n=50):
    print('*' * n)


if __name__ == '__main__':#判断模块是否为主模块
    print(__name__)
    print(__doc__)
    print(__file__)

