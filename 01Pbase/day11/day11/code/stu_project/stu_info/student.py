# file: stu_info/student.py

# 用于存放学生类

class Student:
    def __init__(self, n, a, s):
        self.name = n  # 对象的姓名
        self.age = a  # 年龄
        self.score = s  # 成绩

    def __del__(self):
        print(self.name, '对象已经被销毁')

    def write_to_file(self, fw):
        fw.write(self.name)
        fw.write(',')
        fw.write(str(self.age))
        fw.write(',')
        fw.write(str(self.score))
        fw.write('\n')





