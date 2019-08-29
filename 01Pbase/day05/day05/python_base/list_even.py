# 输入一个开始的整数begin
# 输入一个结束的整数end
# 将从begin到end的所有的偶数存放到列表中
# 打印列表
begin = int(input('请输入开始的整数'))
end = int(input('请输入结束的整数'))
L = [i for i in range(begin,end+1) if i % 2 == 0]
print(L)