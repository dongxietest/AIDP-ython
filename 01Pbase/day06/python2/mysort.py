def mysort(list):
    #1.传入的是可变对象
    #2.函数内容修改的是传入的对象
    #满足以上两点 就无需通过返回值传递结果
    for r in range(0,len(list)-1):
        for c in range(r+1,len(list)):
            if list[r] > list[c]:
                list[r],list[c] = list[c],list[r]

list = [43,4,5,8,12]
mysort(list)
print(list)