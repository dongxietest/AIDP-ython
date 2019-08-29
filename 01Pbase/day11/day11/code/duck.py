# 此示例示意多态的用法
class Animal:
    def move(self):
        print('动物在移动')

class Fish:
    def move(self):
        print("鱼在游")

class Cat:
    def move(self):
        print("猫在走")
class Ship:  # 船
    def move(self):
        print("船在游")

L = [Cat(), Fish(), Ship()]
for x in L:
    x.move()

# a_animal = Cat()
# a_animal.move() # ???
# a_animal = Fish()
# a_animal.move()
# a_animal = Ship()
# a_animal.move()
