L = [4,7,-2,5,-10]
def myabs(x):
    if x<0:
        return -x
    else:
        return x

L2 = sorted(L,key=myabs)
print(L2)