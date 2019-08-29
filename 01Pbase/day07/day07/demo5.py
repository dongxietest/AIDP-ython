def mydeco(fun):
    def fx():
        print('------------')
        fun()
        print('************')
    return fx

@mydeco
def fun():
    print('fun开始运行啦')

# mydeco(fun)
# mydeco(fun)
# mydeco(fun)
fun()
fun()
fun()