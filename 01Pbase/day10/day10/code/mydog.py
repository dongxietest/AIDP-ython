# file : mydog.py
# 　　　　毛色   种类　　　年龄（属性)
# 狗1:   白色   京巴      5
# 狗2:   黑色   导盲犬    6
#
# 行为:
# 吃东西，玩，跑....
class Dog:
    def eat(self, food):
        print("id为", id(self), '的小狗正在吃', food)

    def run(self, speed):
        print('id为', id(self), '的小狗正在跑...', speed)

    def play(self, obj):
        print(self.color, '的', self.kinds, '正在玩',
              obj)
    def happynewyear(self):
        self.age += 1
dog1 = Dog()  # 创建实例
dog2 = Dog()  # 创建实例
dog1.eat('狗粮')
dog2.eat('包子')
dog1.run(100)
dog2.run(10)

dog1.color = '白色'
dog1.kinds = '京巴'
dog1.age = 5
dog1.play('飞盘')

dog2.color = '黑色'
dog2.kinds = '导盲犬'
dog2.age = 6

dog3 = Dog()
# dog3.happynewyear()  # 报错，没有age属性




