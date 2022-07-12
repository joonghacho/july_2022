realation = {
    (1,1) : 1,
    (3,1) : 3,
    (2,2) : 2,
    (0,2) : 0,
    (0,3) : 1,
    (3,3) : 2,
    (1,4) : 2,
    (0,4) : 3,
    (1,5) : 0,
    (2,5) : 3,
    (2,6) : 1,
    (3,6) : 0
}
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def can_move(move_board):
    ori_x = 0
    ori_y = 0
    ori_d = 1
    que = [[ori_x, ori_y, ori_d]]
    cnt = 0
    while que:
        cur = que.pop(0)
        cnt += 1
        cur_x, cur_y, cur_d = cur[0], cur[1], cur[2]
        if cur_x == n-1 and cur_y == n-1:
            return cnt
        next_x = cur_x + dx[cur_d]
        next_y = cur_y + dy[cur_d]
        if (cur_d, move_board[cur_y][cur_x]) not in realation:
            return False
        next_d = realation[(cur_d, move_board[cur_y][cur_x])]
        if board[next_y][next_x] != 0:
            que.append([next_x, next_y, next_d])
    return False

def dfs(index, dfs_board):
    global answer
    if can_move(dfs_board):
        candi = can_move(dfs_board)
        answer = min(answer, candi)
        return
    for k in range(index, len(pipe_list)):
        if pipe_list[k][2] == 0:
            continue
        pipe_list[k][2] -= 1
        pipe_list[k][3] -= 1
        dfs(index + 1, dfs_board)
        pipe_list[k][2] += 1
        pipe_list[k][3] += 1

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        n = int(input())
        board = []
        for _ in range(n):
            line = list(map(int, input().split()))
            board.append(line)
        pipe_list = []
        # pipe_ele = [x, y, 종류 1 or 3, 2 or 6]
        for j in range(n):
            for i in range(n):
                if board[j][i] == 1 or board[j][i] == 2:
                    board[j][i] = 2
                    pipe_list.append([i, j, 1, 2])
                elif board[j][i] == 3 or board[j][i] == 4 or board[j][i] == 5 or board[j][i] == 6:
                    board[j][i] = 6
                    pipe_list.append([i, j, 3, 6])
        answer = n ** 2
        dfs(0, board)
        print(answer)

