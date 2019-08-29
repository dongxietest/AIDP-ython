# 练习 定义函数 根据年月日 返回星期数
#思路 年 月 日  --> 字符串 --> 时间元组
#时间元组 --> 星期  -->  格式
import time

def get_week(year,month,day):
    str_time = '%d-%d-%d' % (year,month,day)
    tuple_time = time.strptime(str_time,'%Y-%m-%d')
    week_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日'
    }
    #
    return week_dict[tuple_time[6]]

print(get_week(2019,7,14))
# print(get_week(20190,7,14))
