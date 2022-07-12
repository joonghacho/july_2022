def search(n, node, computers, visited):
    que = [node]
    visited[node] = 1
    while que:
        start = que.pop(0)
        for i in range(n):
            if computers[start][i] != 0 and visited[i] == 0:
                visited[i] = 1
                que.append(i)
    
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        computers[i][i] = 0
    for node in range(n):
        if visited[node] == 0:
            search(n, node, computers, visited)
            answer += 1
    # print(visited)
    return answer

sol = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print(sol)