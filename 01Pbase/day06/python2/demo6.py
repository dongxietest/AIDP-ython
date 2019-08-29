def call_fun(fn):
    L = [1,3,5,7,9]
    return fn(L)

print(call_fun(max))#max(L)
print(call_fun(min))#min(L)