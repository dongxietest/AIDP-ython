# file: stu_info/controller.py

from .menu import show_menu
from .student import Student

def output_student(L):
    for i, stu in enumerate(L):
        print(i, ': 姓名:', stu.name,
              ' 年龄:', stu.age,
              ' 成绩:', stu.score)

def add_student(L):
    n = input("请输入姓名: ")
    a = int(input("请输入年龄: "))
    s = int(input('请输入成绩: '))
    L.append(Student(n, a, s))

def del_student(L):
    n = int(input('请输入您要删除学生的序号:'))
    try:
        del L[n]
        print("删除成功!")
    except IndexError:
        print("删除失败!")
    # for i, stu in enumerate(L):
    #     if i == n:
    #         del L[i]
    #         print("删除成功!")
    #         return
    # print("删除失败")

def output_student_by_score_desc(L):
    '''按成绩自高至低显示'''
    L2 = sorted(L, key=lambda stu: stu.score, reverse=True)
    output_student(L2)

def output_student_by_score_asc(L):
    L2 = sorted(L, key=lambda stu: stu.score)
    output_student(L2)

def read_from_text_file():
    L = []
    fr = open("si.txt", 'r')
    for line in fr:  # '小张,20,100\n'
        line = line.strip()  # '小张,20,100'
        n, a, s = line.split(',')
        a = int(a)  # 把字符串转为整数
        s = int(s)
        L.append(Student(n, a, s))
    fr.close()
    return L

def save_to_text_file(L):
    fw = open("si.txt", 'w')
    for stu in L:
        stu.write_to_file(fw)
        # fw.write(stu.name)
        # fw.write(',')
        # fw.write(str(stu.age))
        # fw.write(',')
        # fw.write(str(stu.score))
        # fw.write('\n')
    fw.close()

def read_from_csv_file():
    pass

def save_to_csv_file(L):
    fw = open("infos.csv", 'wb')
    for stu in L:
        s = stu.name
        s += ','
        s += str(stu.age) + ','
        s += str(stu.score) + '\r\n'
        b = s.encode('gbk')
        fw.write(b)
    fw.close()




def run():
    infos = [
        Student('小张', 20, 100),
        Student('小李', 18, 68),
        Student('小王', 18, 98),
        Student('小赵', 18, 99),
        Student('小魏', 18, 88),
    ]  # 存入所有学生信息的列表
    while True:
        show_menu()
        s = input("请选择:")
        if s == '1':
            add_student(infos)
        elif s == '2':
            output_student(infos)
        elif s == '3':
            del_student(infos)
        elif s == '4':
            pass
        elif s == '5':
            output_student_by_score_desc(infos)
        elif s == '6':
            output_student_by_score_asc(infos)
        elif s == '7':
            pass
        elif s == '8':
            pass
        elif s == '9':
            infos = read_from_text_file()
        elif s == '10':
            save_to_text_file(infos)
        elif s == '11':
            save_to_csv_file(infos)
        elif s == '12':
            infos = read_from_csv_file()
        elif s == 'q':
            break;
