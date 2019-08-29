import time

# print(time.time())#返回当前时间距计算机元年的总秒数
# print(time.localtime())#返回当前时间的时间元组
# t = time.localtime()
# print(time.mktime(t))#将时间元组转换成时间戳

# print('程序正在运行')
# time.sleep(10)#将程序暂时挂起 秒
# print('程序运行结束')

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strptime('2019-07-14','%Y-%m-%d'))