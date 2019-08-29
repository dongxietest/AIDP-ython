# file : mydog.py
# 　　　　毛色   种类　　　年龄（属性)
# 狗1:   白色   京巴      5
# 狗2:   黑色   导盲犬    6
#
# 行为:
# 吃东西，玩，跑....
class Dog2:
    def __init__(self, clr, kinds, age=1):
        '''此方法为初始化方法'''
        print("__init__被调用, id(self)=", id(self))
        # 为self对象添加color , kinds, age 三个属性, 用来
        # 绑定传入的数据
        self.color = clr
        self.kinds = kinds
        self.age = age

    def eat(self, food):
        print("id为", id(self), '的小狗正在吃', food)

    def play(self, obj):
        print(self.color, '的', self.kinds, '正在玩',
              obj)
dog1 = Dog2('白色', '京巴', 5)  # 创建实例
dog2 = Dog2('黑色', '导盲犬')  # 创建实例
dog1.eat('狗粮')
dog2.eat('包子')
dog1.play('飞盘')
dog2.play('皮球')

# dog2.age = 6





