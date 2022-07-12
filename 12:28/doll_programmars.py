def get_score(box, ele, score):
    if len(box) == 0:
        box.append(ele)
        return 0
    last_ele = box[-1]
    if ele == last_ele:
        box.pop()
        return 2
    else:
        box.append(ele)
        return 0

def solution(board, moves):
    board_size = len(board)
    new_board = [[] for _ in range(board_size)]
    for i in range(board_size):
        for line in board:
            if line[i] != 0:
                new_board[i].append(line[i])
    # print(new_board)
    box = []
    score = 0
    for move in moves:
        if new_board[move-1] != []:
            ele = new_board[move-1].pop(0)
            score += get_score(box, ele, score)
    answer = score
    return answer

sol = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(sol)