dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def breed(que_ele, my_que):
    if que_ele[3] == que_ele[2] + 1:
        for direc in range(4):
            next_x = que_ele[0] + dx[direc]
            next_y = que_ele[1] + dy[direc]
            if my_map[next_y][next_x][0] == 0:
                my_map[next_y][next_x] = [que_ele[2], 1]
                my_que.append([next_x, next_y, que_ele[2], 1])
            else:
                if my_map[next_y][next_x][1] == 1:
                    if my_map[next_y][next_x][0] < que_ele[2]:
                        my_map[next_y][next_x] = [que_ele[2], 1]
                        # my_que.append([next_x, next_y, que_ele[2], 1])
    return

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    my_map = [[[0,0] for _ in range(400)] for _ in range(400)]
    # my_map_ele = [lifeX, ori = -1 new = 1]
    init_map = []
    for _ in range(n):    
        line = list(map(int, input().split()))
        init_map.append(line)
    que = []
    # que_ele = [cur_x, cur_y, lifeX, cur_state]
    for j in range(n):
        for i in range(m):
            if init_map[j][i] != 0:
                my_map[j+160][i+160] = [init_map[j][i], -1]
                que.append([i+160, j+160, init_map[j][i], 1])
    for time in range(2, k+1):
        new_que = []
        for que_ele in que:
            my_map[que_ele[1]][que_ele[0]][1] = -1
            que_ele[3] += 1    
            breed(que_ele, new_que)
        que = que + new_que
        del_que = []
        for que_del_ele in que:
            if que_del_ele[3] < que_del_ele[2] * 2:
                del_que.append(que_del_ele)
        que = del_que
        print(que)
        print(len(que))
    # for que_last_del in que:
    #     if que_last_del[3] <= que_last_del[2] * 2:
    #         del_que.append(que_last_del)
    # que = del_que
    # print(len(que))
