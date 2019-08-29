


_map_data = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

# _map_data = [
#     [2, 2, 4, 2],  # 左操作 --> [4, 4, 2, 0]
#     [0, 2, 8, 2],
#     [0, 0, 0, 4],
#     [0, 0, 0, 2],
# ]


def _left_move_number(line):
    '''把数字靠左，右侧填0'''
    #　算法
    for _ in range(3):
        for i in range(3):  # i -> 0, 1, 2
            if line[i] == 0:
                line[i] = line[i+1]
                line[i+1] = 0

def _left_merge_number(line):
    # line = [2, 2, 4, 4]  # [4, 0, 8, 0]
    for i in range(3):
        if line[i] == line[i+1]:
            line[i] *= 2
            line[i+1] = 0

def _left_move_aline(line):
    _left_move_number(line)
    _left_merge_number(line)
    _left_move_number(line)

# def test():
#     L = [2, 2, 4, 4]  # [4, 0, 8, 0]
#     _left_move_aline(L)
#     print(L)  # [4, 8, 0, 0]
#
# test()


def show_map():
    '用字符界面显示地图'
    for line in _map_data:
        print(line)

def left():
    for line in _map_data:
        _left_move_aline(line)

def right():
    for line in _map_data:
        line.reverse()  # 当前行左右互换
        _left_move_aline(line)
        line.reverse()  # 当前行左右互换

def up():
    for col in range(4):  # col 代表当前列索引
        line = [0, 0, 0, 0]
        for row in range(4):
            line[row] = _map_data[row][col]
        _left_move_aline(line)  # 当前列上左移
        for row in range(4):  # 放回原位
            _map_data[row][col] = line[row]

def down():
    _map_data.reverse()
    up()
    _map_data.reverse()

def get_space_count():
    '''得到地图中0的个数'''
    count = 0
    for line in _map_data:
        count += line.count(0)
    return count

def fill2():
    count = get_space_count()
    if count == 0:
        return  # 没地方填充
    import random
    pos = random.randrange(count)
    offset = 0
    for row in _map_data:   # row为行row
        for col in range(4):  # col 为列，column
            if row[col] == 0:
                if pos == offset:
                    row[col] = 2
                    return
                offset += 1  #  接着向下找

def main():
    while True:
        show_map()
        print("0的个数是:", get_space_count())
        s = input("请输入方向:")
        if s == 'a':  # 向左
            left()
            fill2()
        elif s == 'd':  # 右
            right()
            fill2()
        elif s == 'w':  # 上
            up()
            fill2()
        elif s == 's':  # 向下
            down()
            fill2()
        elif s == 'q':  # 退出
            break

if __name__ == '__main__':
    main()


