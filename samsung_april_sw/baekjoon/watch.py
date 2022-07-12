import copy
from itertools import product

n, m = map(int, input().split())
my_map = []
for _ in range(n):
    line = list(map(int, input().split()))
    my_map.append(line)

cctvs = []

for j in range(n):
    for i in range(m):
        if my_map[j][i] == 1:
            cctv_1 = []
            for i_1 in range(4):
                cctv_1.append([i,j,1,i_1])
            cctvs.append(cctv_1)
        elif my_map[j][i] == 2:
            cctv_2 = []
            for i_2 in range(2):
                cctv_2.append([i,j,2,i_2])
            cctvs.append(cctv_2)
        elif my_map[j][i] == 3:
            cctv_3 = []
            for i_3 in range(4):
                cctv_3.append([i,j,3,i_3])
            cctvs.append(cctv_3)
        elif my_map[j][i] == 4:
            cctv_4 = []
            for i_4 in range(4):
                cctv_4.append([i,j,4,i_4])
            cctvs.append(cctv_4)
        elif my_map[j][i] == 5:
            cctv_5 = []
            for i_5 in range(1):
                cctv_5.append([i,j,5,i_5])
            cctvs.append(cctv_5)

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def watching(test_map, cctv_x, cctv_y, cctv_num, direction):
    if cctv_num == 1:
        next_x = cctv_x + dx[direction%4]
        next_y = cctv_y + dy[direction%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[direction%4]
            next_y += dy[direction%4]
    elif cctv_num == 2:
        next_x = cctv_x + dx[direction%4]
        next_y = cctv_y + dy[direction%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[direction%4]
            next_y += dy[direction%4]
        next_x = cctv_x + dx[(direction-2)%4]
        next_y = cctv_y + dy[(direction-2)%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[(direction-2)%4]
            next_y += dy[(direction-2)%4]
    elif cctv_num == 3:
        next_x = cctv_x + dx[direction%4]
        next_y = cctv_y + dy[direction%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[direction%4]
            next_y += dy[direction%4]
        next_x = cctv_x + dx[(direction-1)%4]
        next_y = cctv_y + dy[(direction-1)%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[(direction-1)%4]
            next_y += dy[(direction-1)%4]
    elif cctv_num == 4:
        next_x = cctv_x + dx[direction%4]
        next_y = cctv_y + dy[direction%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[direction%4]
            next_y += dy[direction%4]
        next_x = cctv_x + dx[(direction-1)%4]
        next_y = cctv_y + dy[(direction-1)%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[(direction-1)%4]
            next_y += dy[(direction-1)%4]
        next_x = cctv_x + dx[(direction-2)%4]
        next_y = cctv_y + dy[(direction-2)%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[(direction-2)%4]
            next_y += dy[(direction-2)%4]
    elif cctv_num == 5:
        next_x = cctv_x + dx[direction%4]
        next_y = cctv_y + dy[direction%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[direction%4]
            next_y += dy[direction%4]
        next_x = cctv_x + dx[(direction-1)%4]
        next_y = cctv_y + dy[(direction-1)%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[(direction-1)%4]
            next_y += dy[(direction-1)%4]
        next_x = cctv_x + dx[(direction-2)%4]
        next_y = cctv_y + dy[(direction-2)%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[(direction-2)%4]
            next_y += dy[(direction-2)%4]
        next_x = cctv_x + dx[(direction-3)%4]
        next_y = cctv_y + dy[(direction-3)%4]
        while 0 <= next_y < n and 0 <= next_x < m and test_map[next_y][next_x] != 6:
            if test_map[next_y][next_x] == 0:
                test_map[next_y][next_x] = "#"
            next_x += dx[(direction-3)%4]
            next_y += dy[(direction-3)%4]
    
def count(my_map):
    count = 0
    for j in range(n):
        for i in range(m):
            if my_map[j][i] == 0:
                count += 1
    return count

answer = 64
# print(cctvs)
combies = []
for t in product(*cctvs):
    combies.append(t)

# for iiii in combies:
#     print(iiii)
#     print("---")

for real_candi in combies:
    test_map = copy.deepcopy(my_map)
    for cctv_candi in real_candi:
        # print(cctv_candi, "cctv_candi")
        watching(test_map, cctv_candi[0], cctv_candi[1], cctv_candi[2], cctv_candi[3])
        answer_candi = count(test_map)
        if answer > answer_candi:
            answer = answer_candi
            
print(answer)