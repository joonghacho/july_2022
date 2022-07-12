import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, l, r = map(int, input().split())
board = []
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

# point = [x, y]
def get_group(point, get_visited):
    que = [point]
    my_group = []
    while que:
        cur_point = que.pop(0)
        if get_visited[cur_point[1]][cur_point[0]] == 0:
            get_visited[cur_point[1]][cur_point[0]] = 1
            my_group.append([cur_point[0], cur_point[1]])
            for direction in range(4):
                next_x = cur_point[0] + dx[direction]
                next_y = cur_point[1] + dy[direction]
                if 0 <= next_x < n and 0 <= next_y < n and get_visited[next_y][next_x] == 0 and l <= abs(board[cur_point[1]][cur_point[0]] - board[next_y][next_x]) <= r:
                    que.append([next_x, next_y])
    return my_group

def get_groups():
    visited = [[0 for _ in range(n)] for _ in range(n)]
    groups = []
    for j in range(n):
        for i in range(n):
            candi_group = get_group([i, j], visited)
            if candi_group != []:
                groups.append(candi_group)
    return groups

def moving(moving_groups):
    # print("moving_groups", (moving_groups))
    if len(moving_groups) == n**2:
        return False
    for group_ele in moving_groups:
        if len(group_ele) != 1:
            group_ele_sum = 0
            group_ele_num = len(group_ele)
            for nation in group_ele:
                group_ele_sum += board[nation[1]][nation[0]]
            for nation in group_ele:
                board[nation[1]][nation[0]] = (group_ele_sum // group_ele_num)
    return True

can_move = True
answer = -1
while(can_move):
    can_move = moving(get_groups())
    # print("can_move", can_move)
    answer += 1
# print(board)
print(answer)
# print(moving(get_groups()))
