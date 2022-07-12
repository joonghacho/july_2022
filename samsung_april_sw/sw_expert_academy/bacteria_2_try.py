dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def breed(my_cells):
    new_cells = []
    for cell in my_cells:
        if board[cell[1]][cell[0]][1] < 0:
            for direction in range(4):
                next_x = cell[0] + dx[direction]
                next_y = cell[1] + dy[direction]
                if board[next_y][next_x] == [0,0]:
                    new_cells.append([next_x, next_y, cell[2]])
    return new_cells

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    board = [[[0,0] for _ in range(m + k + 1)] for _ in range(n + k + 1)]
    init_board = []
    cells = []
    # cell = [x, y, life]
    for _ in range(n):
        line = list(map(int, input().split()))
        init_board.append(line)
    for j in range(n):
        for i in range(m):
            if init_board[j][i] >= 1:
                x = init_board[j][i]
                board[j+k//2][i+k//2] = [x, x] #[life, age]
                cells.append([i+k//2, j+k//2, x])
    
    for time in range(1, k+1):
        for jj in range(n + k + 1):
            for ii in range(m + k + 1):
                if board[jj][ii][0] != 0:
                    board[jj][ii][1] -= 1
        new_cells = breed(cells)
        for new_cell in new_cells:
            if board[new_cell[1]][new_cell[0]] == 0:
                board[new_cell[1]][new_cell[0]] = [new_cell[2], new_cell[2]]
            else:
                if new_cell[2] > board[new_cell[1]][new_cell[0]][0]:
                    board[new_cell[1]][new_cell[0]] = [new_cell[2], new_cell[2]]
        cells = []
        for jjj in range(n + k + 1):
            for iii in range(m + k + 1):
                if board[jjj][iii][0] != 0:
                    cells.append([iii, jjj, board[jjj][iii][0]])
        # print("cells", cells)
        # print("new_cells:", new_cells)
        # for kkkkk in board:
        #     print(kkkkk)
        # print("------------")

    answer = 0
    for jjjj in range(n + k + 1):
        for iiii in range(m + k + 1):
            if board[jjjj][iiii][0] != 0 and board[jjjj][iiii][1] > board[jjjj][iiii][0] * (-1):
                answer += 1
    print("#" + str(test_case) + " " + str(answer))