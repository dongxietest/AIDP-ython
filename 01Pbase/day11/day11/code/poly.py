# 此示例示意多态的用法
class Animal:
    def move(self):
        print('动物在移动')

class Fish(Animal):
    def move(self):
        print("鱼在游")

class Cat(Animal):
    def move(self):
        print("猫在走")

a_animal = Cat()
a_animal.move() # ???
a_animal = Fish()
a_animal.move()
