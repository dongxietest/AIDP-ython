# 在原有的功能上 为取钱添加一个验证功能
# 当用户取钱时 打印正在进行权限验证...
# 在原有的功能上 添加短信通知功能
# 当用户存钱或取钱时 打印正在向用户发送短信
# 休息+练习 15:35~15:50
def priv_check(fn):
    def fx(n,m):
        print('正在进行权限验证')
        fn(n,m)
    return fx

def send_message(fn):
    def fy(n,m):
        fn(n,m)
        print('向',n,'发送短信')
    return fy
#假设银行系统业务有存钱和取钱
@send_message
def savemoney(name,money):
    print(name,'存了',money,'元')

@send_message
@priv_check
def withdraw(name,money):
    print(name,'取了',money,'元')


savemoney('老王',500)
savemoney('小郭',1000)
withdraw('老魏',10000)