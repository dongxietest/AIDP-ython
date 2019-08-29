# 练习：
# 定义函数 根据年和月 计算有多少天  考虑2月闰年29天 平年28天

#判断年份是否为闰年
def is_leap_year(year):
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # else:
    #     return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_day(year,month):
     if month < 1 or month > 12:
         return 0
     if month == 2:
         # if is_leap_year(year):
         #     return 29
         # else:
         #     return 28
         return 29 if is_leap_year(year) else 28
     if month in (4,6,9,11):
         return 30
     else:
         return 31

get_day(2019,6)#30