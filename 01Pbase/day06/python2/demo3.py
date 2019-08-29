def fun(list = []):
    list.append('***')
    print(list)
    print(id(list))

list = [1,2,3]
fun(list)
print('***************')
fun()
print('***************')
fun()



