

# file: myinteger.py

def myinteger(end):
    i = 0
    while i < end:
        yield i
        i += 1

for x in myinteger(1000000000000000000):
    print(x)

