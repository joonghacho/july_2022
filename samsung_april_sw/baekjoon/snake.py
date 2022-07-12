import sys
from collections import deque

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    j, i = map(int, input().split())
    apples.append([j, i])
my_map = [[-1 for _ in range(n+2)] for _ in range(n+2)]
for col in range(n):
    for row in range(n):
        my_map[col+1][row+1] = 0
for apple in apples:
    my_map[apple[0]][apple[1]] = 2

# print(my_map)

dict_for_rotate = dict()
l = int(input())
for _ in range(l):
    x, c = sys.stdin.readline().split()
    dict_for_rotate[int(x)] = c

# print(dict_for_rotate)

# wall -1, empty 0, apple 2

def rotate(cur, direction):
    if direction == "D":
        if cur == (1, 0):
            return (0, 1)
        elif cur == (0, 1):
            return (-1, 0)
        elif cur == (-1, 0):
            return (0, -1)
        else:
            return (1, 0)
    else:
        if cur == (1, 0):
            return (0, -1)
        elif cur == (0, -1):
            return (-1, 0)
        elif cur == (-1, 0):
            return (0, 1)
        else:
            return (1, 0)

cur = (1, 0)
my_deq = deque()
my_deq.append([1, 1])
answer = 0

while True:
    #print(my_deq, "my_deq")
    answer += 1
    dx, dy = cur
    head_x, head_y = my_deq[0][1], my_deq[0][0]
    if my_map[head_y+dy][head_x+dx] == -1:
        break
    if [head_y+dy, head_x+dx] in my_deq:
        break
    if my_map[head_y+dy][head_x+dx] == 0:
        my_deq.appendleft([head_y+dy, head_x+dx])
        my_deq.pop()
    elif my_map[head_y+dy][head_x+dx] == 2:
        my_deq.appendleft([head_y+dy, head_x+dx])
        my_map[head_y+dy][head_x+dx] = 0
    if answer in dict_for_rotate:
        cur = rotate(cur, dict_for_rotate[answer])    
print(answer)