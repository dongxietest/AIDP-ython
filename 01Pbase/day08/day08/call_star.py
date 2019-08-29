# import star
#
# print(star.hi)
# star.pstar()
from star import hi,pstar
# from star import *
# print(hi)
# pstar()
from color import color

@color(31)
def hello(word):
    return 'hello %s' % word

print(hello('China'))

