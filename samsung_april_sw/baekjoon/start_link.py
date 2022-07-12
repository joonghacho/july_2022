import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
my_map = []
people = [0] * n
for _ in range(n):
    line = list(map(int, input().split()))
    my_map.append(line)

answer = 4000000

def dfs(count, index):
    global answer
    if count == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if people[i] and people[j]:
                    start += my_map[i][j]
                elif not people[i] and not people[j]:
                    link += my_map[i][j]
        candi = abs(start - link)
        answer = min(answer, candi)
        return
    for k in range(index, n):
        if people[k]:
            continue
        people[k] = 1
        dfs(count + 1, index + 1)
        people[k] = 0

dfs(0, 0)
print(answer)