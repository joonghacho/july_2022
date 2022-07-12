n, m = map(int, input().split())
r, c, d = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
room = []
for _ in range(n):
    line = list(map(int, input().split()))
    room.append(line)

def check_empty(room, cur_x, cur_y, d):
    candi_d = (d - 1) % 4
    new_x = cur_x + dx[candi_d]
    new_y = cur_y + dy[candi_d]
    if room[new_y][new_x] == 0:
        return 0
    else:
        return 1

cur_loca = [c, r]
count = 0
answer = 1
room[cur_loca[1]][cur_loca[0]] = -1
while True:
    if count == 4:
        back_d = (d - 2) % 4
        back_x = cur_loca[0] + dx[back_d]
        back_y = cur_loca[1] + dy[back_d]
        if room[back_y][back_x] == 1:
            break
        else:
            cur_loca[0] += dx[back_d]
            cur_loca[1] += dy[back_d]
            count = 0
    if check_empty(room, cur_loca[0], cur_loca[1], d) == 0:
        d = (d - 1) % 4
        cur_loca[0] += dx[d]
        cur_loca[1] += dy[d]
        answer += 1
        room[cur_loca[1]][cur_loca[0]] = -1
        count = 0
    else:
        d = (d - 1) % 4
        count += 1

print(answer)
