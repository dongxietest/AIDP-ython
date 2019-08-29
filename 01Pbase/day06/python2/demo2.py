# def mysum(num1,num2):
#    print('num1：',num1)
#    print('num2：',num2)

#位置传参 实参的个数必须与形参的个数相同
# mysum(10,20)
# mysum(20,10)
# mysum(10)#TypeError: mysum() missing 1 required positional argument: 'num2'
# mysum(10,20,30)#TypeError: mysum() takes 2 positional arguments but 3 were given

#序列传参
# 用*拆解序列后按照位置来依次对应传参
# list = [10,20]
# mysum(*list)


#关键字传参 可以不按位置进行匹配
# mysum(num1=20,num2=10)
# mysum(num2=10,num1=20)

#字典传参
#用**将字典拆解 拆解后成为键=值的关键字格式 然后使用关键字传参
# dict = {'num1':10,'num2':20}
# mysum(**dict)#num1=20,num2=10

def fun(a,b,c,d):
    print('a：', a)
    print('b：', b)
    print('c：', c)
    print('d：', d)

# fun(1,2,3,4)
# fun(a=1,c=3,b=2,d=4)
# fun(1,2,c=5,d=6)
# fun(c=5,d=6,1,2)#SyntaxError: positional argument follows keyword argument




