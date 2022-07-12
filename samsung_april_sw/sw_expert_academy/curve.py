dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# curve = [[start_x, start_y], [x,y]]
def get_next_curve(ori_curve):
    last_ele = ori_curve[-1]
    end_curve = ori_curve[::-1]
    diff_curve = []
    for end_i in range(1, len(end_curve)):
        diff_ele = []
        diff_ele.append(-1*(end_curve[end_i][1] - last_ele[1]))
        diff_ele.append((end_curve[end_i][0] - last_ele[0]))
        diff_curve.append(diff_ele)
    plus_curve = []
    for ii in range(len(diff_curve)):
        plus_ele = []
        plus_ele.append(last_ele[0] + diff_curve[ii][0])
        plus_ele.append(last_ele[1] + diff_curve[ii][1])
        plus_curve.append(plus_ele)
    return ori_curve + plus_curve

# print(get_next_curve([[0, 0], [1, 0], [1, -1]]))

n = int(input())
curves = []
for _ in range(n):
    curve = list(map(int, input().split()))
    curves.append(curve)

real_curve = []
for each_curve in curves:
    cur_curve = []
    cur_curve.append([each_curve[0], each_curve[1]])
    cur_curve.append([each_curve[0] + dx[each_curve[2]], each_curve[1] + dy[each_curve[2]]])
    for change in range(each_curve[3]):
        cur_curve = get_next_curve(cur_curve)
    real_curve.append(cur_curve)

# print(real_curve)
board = [[0 for _ in range(100)] for _ in range(100)]
for real_ele in real_curve:
    # print(real_ele)
    for point in real_ele:
        board[point[1]][point[0]] = 1
answer = 0
for y in range(1, 100):
    for x in range(1, 100):
        if board[y][x] == 1 and board[y-1][x] == 1 and board[y][x-1] == 1 and board[y-1][x-1] == 1:
            answer += 1
print(answer)