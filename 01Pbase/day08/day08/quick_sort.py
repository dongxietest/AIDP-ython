'''快速排序思路：
1.假设列表中的第一个数是中间值，将比它小的数字放到smaller
列表中，将比它大的数放到larger列表中
2.因为smaller列表和larger列表也是无序的，需要继续使用相同
的方式分割
3.如果列表的长度是0或1，就没有必要再次继续排序
'''
def quick_sort(num_list):
    if len(num_list) < 2:
        return num_list

    middle = num_list[0]
    smaller = []
    larger = []
    for i in num_list[1:]:
        if i < middle:
            smaller.append(i)
        else:
            larger.append(i)
    return quick_sort(smaller)+[middle]+quick_sort(larger)

alist = [8,2,15,22,7,8]
print(quick_sort(alist))