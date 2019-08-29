# 2.生成随机密码
# 要求密码内容为0-9 a-z A-Z
# 随机生成任意位数的密码
from random import choice
import string

__all__ = ['randpass']

all_chs = string.ascii_letters+string.digits
def randpass(n):
    result = ''
    for i in range(n):
        ch = choice(all_chs)
        result += ch
    return result

if __name__ == '__main__':
    print(randpass(8))
    print(randpass(4))