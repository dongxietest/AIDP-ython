import random
from randpass import *

alist = [i for i in range(1,11)]

print(random.randint(0,2))
print(random.choice(alist))

random.shuffle(alist)
print(alist)

randpass(18)
print(all_chs)
