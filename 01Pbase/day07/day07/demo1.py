# s = 'x = 10\ny = 20\nprint(x+y)'
# exec(s)
#
# s = 'x = 10;y = 20;print(x+y)'
# exec(s)
#
# s = '''
# ... x = 10
# ... y = 20
# ... print(x+y)'''
# exec(s)
# x = 100
# y = 200
# s = 'x+y'
# # val = eval(s)
# # print(val)
#
# val2 = eval(s,None,{'x':1,'y':2})#优先使用局部
# print(val2)
#
# val3 = eval(s,None,{'y':20})
# print(val3)
s = """
x = 100
y = 200
z = x+y
print(x,'+',y,'=',z)
"""
global_dict = {}
exec(s,global_dict)
for k in global_dict:
    print(k)




