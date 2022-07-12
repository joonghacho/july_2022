dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def shark_move(shark, move_board):
    if move_board[shark[0]][shark[1]][2] == shark[4]:
        move_board[shark[0]][shark[1]] = [0, 0, 0]
    next_y = shark[0]
    next_x = shark[1]
    for time in range(shark[2]):
        next_y += dy[shark[3]]
        next_x += dx[shark[3]]
        # print(next_x, next_y, "location")
        if shark[3] == 1 or shark[3] == 1:
            if next_x <= 0 or next_x >= c-1:
                shark[3] = (shark[3] - 2) % 4
        else:
            if next_y <= 0 or next_y >= r-1:
                shark[3] = (shark[3] - 2) % 4
    if move_board[next_y][next_x][2] < shark[4]:
        move_board[next_y][next_x][0] = shark[2]
        move_board[next_y][next_x][1] = shark[3]
        move_board[next_y][next_x][2] = shark[4]

def sharks_all_move(sharks_list, all_move_board):
    for each_shark in sharks_list:
        shark_move(each_shark, all_move_board)
    new_shark_list = []
    for jj in range(r):
        for ii in range(c):
            if all_move_board[jj][ii] != [0,0,0]:
                new_shark_list.append([jj, ii, all_move_board[jj][ii][0], all_move_board[jj][ii][1], all_move_board[jj][ii][2]])
    return new_shark_list

r, c, m = map(int, input().split())
sharks = []
# shark = [r, c, speed, direction, size]
for _ in range(m):
    shark_ele = []
    y, x, speed, direction, size = map(int, input().split())
    shark_ele.append(y-1)
    shark_ele.append(x-1)
    shark_ele.append(speed)
    if direction == 1:
        shark_ele.append(0)
    elif direction == 2:
        shark_ele.append(2)
    elif direction == 3:
        shark_ele.append(1)
    else:
        shark_ele.append(3)
    shark_ele.append(size)
    sharks.append(shark_ele)

board = [[[0, 0, 0] for _ in range(c)] for _ in range(r)]
for board_shark in sharks:
    board[board_shark[0]][board_shark[1]] = [board_shark[2], board_shark[3], board_shark[4]]

answer = 0
for person in range(c):
    # print(person)
    for height in range(r):
        if board[height][person][2] != 0:
            # print(height, person, "dd")
            candidate_height = height
            candidate_person = person
            board[height][person][2] = 0
            # print(candidate)
            for candi_shark_i in range(len(sharks)):
                # print(sharks[candi_shark_i])
                # print((sharks[candi_shark_i][0], sharks[candi_shark_i][1]))
                if sharks[candi_shark_i][0] == candidate_height and sharks[candi_shark_i][1] == candidate_person:
                    answer_candi = sharks[candi_shark_i]
                    answer += answer_candi[4]
                    print(answer_candi[4], person)
            del sharks[candi_shark_i]
            break
    sharks = sharks_all_move(sharks, board)
print(answer)
