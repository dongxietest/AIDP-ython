#根据小时、分钟、秒计算总秒数
#可以只写小时 ->  秒
#可以只写分钟 ->  秒
#可以写小时+分钟   ->  秒
def get_second(hour = 0,minute = 0,second = 0):
    return hour * 3600 + minute * 60 + second

print(get_second())
print(get_second(1))#只写小时
print(get_second(minute=25))#只写分钟
print(get_second(1,25))#写小时 分钟
print(get_second(1,20,30))