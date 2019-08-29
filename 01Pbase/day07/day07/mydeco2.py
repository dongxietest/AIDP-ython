def deco_out1(func):
    print('---out11---')
    def inner1(*args,**kwargs):
        print('---in11---')
        func()
        print('---in12---')
    print('---out12---')
    return inner1

def deco_out2(func):
    print('---out21---')
    def inner2(*args,**kwargs):
        print('---in21---')
        func()
        print('---in22---')
    print('---out22---')
    return inner2

@deco_out2
@deco_out1
def test():
    print('---test---')

test()