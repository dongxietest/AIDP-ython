# 练习：
# 再写一个函数 get_fun(op) 如果传入'+' 返回myadd函数
def get_fun(op):
    def myadd(x,y):
        return x+y
    def mysub(x,y):
        return x-y
    def mymul(x,y):
        return x*y
    def mydiv(x,y):
        return x/y
    #{'+':myadd,'-':mysub,...}   
    if op == '+':
        return myadd
    elif op == '-':
        return mysub
    elif op == '*':
        return mymul
    elif op == '/':
        return mydiv

def main():
    s = input('请输入计算公式') # '10 + 20'
    #根据用户输入 获取x的值10 获取op '+'  获取y的值20
    list = s.split()#['10','+','20']
    x = int(list[0])
    op = list[1]
    y = int(list[2])
    #通过get_fun(op)获取对应函数 计算结果
    fn = get_fun(op)
    #打印结果
    print('结果为：',fn(x,y))

main()








