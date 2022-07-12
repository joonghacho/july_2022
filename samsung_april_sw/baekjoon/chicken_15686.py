dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_distance(house, dist_board):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    que = [[house, 0]]
    while que:
        cur_house = que.pop(0)
        visited[cur_house[0][1]][cur_house[0][0]] = 1
        for direction in range(4):
            next_x = cur_house[0][0] + dx[direction]
            next_y = cur_house[0][1] + dy[direction]
            if 0 <= next_x < n and 0 <= next_y < n and visited[next_y][next_x] == 0 and dist_board[next_y][next_x] == 2:
                return cur_house[1] + 1
            elif 0 <= next_x < n and 0 <= next_y < n and visited[next_y][next_x] == 0 and (dist_board[next_y][next_x] == 1 or dist_board[next_y][next_x] == 0):
                que.append([[next_x, next_y], cur_house[1] + 1])
    return

def get_score(score_house_list, score_board):
    my_score = 0
    for house_ele in score_house_list:
        my_score += get_distance(house_ele, score_board)
    return my_score

def dfs(count, index, dfs_board):
    global answer
    if count == erase_chicken_num:
        candidate = get_score(house_list, dfs_board)
        if candidate < answer:
            answer = candidate
            print(answer)
            print("count", count)
            for ii in dfs_board:
                print(ii)
            return
        return
    for k in range(index, len(chicken_list)):
        if dfs_board[chicken_list[k][1]][chicken_list[k][0]] == 0:
            continue
        dfs_board[chicken_list[k][1]][chicken_list[k][0]] = 0
        dfs(count + 1, index + 1, dfs_board)
        dfs_board[chicken_list[k][1]][chicken_list[k][0]] = 2

n, m = map(int, input().split())

board = []
for _ in range(n):
    line = list(map(int,input().split()))
    board.append(line)
# for i in board:
#     print(i)

house_list = []
chicken_num = 0
chicken_list = []

for j in range(n):
    for i in range(n):
        if board[j][i] == 1:
            house_list.append([i, j])
        elif board[j][i] == 2:
            chicken_num += 1
            chicken_list.append([i, j])

erase_chicken_num = chicken_num - m
answer = 10000000

dfs(0, 0, board)
print(answer)