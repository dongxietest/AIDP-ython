# def fun1():
#    a = 1
#    def fun2():
#       print(a)
#
#    return fun2
#
# fun1()

#压岁钱
def give_gife_money(money):
    '''
    给孩子压岁钱
    :param money:压岁钱
    :return: 孩子花钱购买物品的函数
    '''
    print('孩子得到了%s元' % money)
    def child_buy(target,price):
        '''
        孩子花钱购买商品
        :param target:想要买的商品
        :param price: 商品单价
        :param money: 压岁钱
        :return:
        '''
        #使用外层嵌套函数的变量
        nonlocal money
        #如果购买的物品单价大于压岁钱余额 提示钱不够了
        if price > money:
            print('压岁钱不够用了')
        #否则打印 花了xx元买xxx
        else:
            money -= price
            print('孩子花了%s元,买了%s,还剩%s元' \
                  % (price,target,money))
    return child_buy

action = give_gife_money(10000)
action('手机',8000)
action('键盘',2000)
action('鼠标',600)
print(action.__doc__)






