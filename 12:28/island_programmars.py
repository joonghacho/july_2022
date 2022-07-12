def parent(node, parents):
    if node == parents[node]:
        return node
    else:
        return parent(parents[node], parents)

def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    bridge = 0
    for elements in costs:
        if bridge == n-1:
            return answer
        if parent(elements[0], parents) !=  parent(elements[1], parents):
            answer += elements[2]
            bridge += 1
            parents[parent(elements[0], parents)] = elements[1]
    return answer

sol = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
print(sol)