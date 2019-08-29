# 练习:
# 写一个
# get_score函数:
#
#
# def get_score():
#     s = input("请输入学生成绩:")
#     ...  # 此处把学生成绩 转为0~100之
#     间的整数返回给调用者, 如果输入有误，则
#     返回0
#
#
# score = get_score()
# print("学生的成绩是:", score)
# 要求：　有任何情况下，程序都能正常退

def get_score():
    s = input("请输入学生成绩:")
    try:
        scr = int(s)
    except ValueError:
        return 0
    # 在用if语句进行错误处理
    if scr < 0 or scr > 100:
        return 0
    return scr


score = get_score()
print("学生的成绩是:", score)

