# print('\033[31;1m%s\033[0m' % 'hello world')
# print('\033[32;1m%s\033[0m' % 'hello world')

# def color(func):
#     def red():
#         return '\033[31;1m%s\033[0m' % func()
#     return red
#
# @color
# def hello():
#     return 'hello world'
#
# print(hello())#因为hello有装饰器 所以调用时不是直接调用
#               #而是相当于color(hello)()
#               #color(hello)返回red
#               #color(hello)()相当于 red()



#被装饰函数带参数时
# def color(func):
#     def red(*args):
#         return '\033[31;1m%s\033[0m' % func(*args)
#     return red
#
# @color
# def hello(word):
#     return 'hello %s' % word
#
# print(hello('China'))


# 返回不同颜色的字体
# def color(color):
#     def set_color(func):
#         def red(*args):
#             return '\033[31;1m%s\033[0m' % (func(*args))
#         def green(*args):
#             return '\033[32;1m%s\033[0m' % func(*args)
#         adict = {'red':red,'green':green}
#         return adict[color]
#     return set_color
#
# @color('red')
# def hello(word):
#     return 'hello %s' % word
#
# @color('green')
# def welcome():
#     return 'Welcome to China'
#
# print(hello('China'))
# print(welcome())

def color(color):
    def set_color(func):
        def show(*args,**kwargs):
            return '\033[%d;1m%s\033[0m' % (color,func(*args))
        return show
    return set_color








