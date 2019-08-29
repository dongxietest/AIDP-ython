# 1.猜数字游戏
# 随机生成一个0`100的整数
# 让用户输入数字 输出猜数字的结果
# 直到猜对 才退出
import random
num = random.randint(0,100)
running = True
def guess():
    answer = int(input('guess the number:'))
    if answer == num:
        print('猜对了')
        global running
        running = False
    elif answer < num:
        print('猜小了')
    else:
        print('猜大了')

if __name__ == '__main__':
    while running:
        guess()
