def solution(n, costs):
    islands = [[10000 for _ in range(n)] for _ in range(n)]
    for bridge in costs:
        islands[bridge[0]][bridge[1]] = bridge[2]
        islands[bridge[1]][bridge[0]] = bridge[2]
    # for iii in islands:
    #     print(iii)
    
    answer = 0
    visited = [0]
    while len(visited) != n:
        my_island = islands[0]
        tmp_min = 10000
        for can in range(len(my_island)):
            if can not in visited:
                if my_island[can] < tmp_min:
                    tmp_min = my_island[can]
        for can_min_i in range(len(my_island)):
            if can_min_i not in visited:
                if my_island[can_min_i] == tmp_min:
                    min_i = can_min_i
        score = merge_and_count(islands, min_i, tmp_min)
        # print(min_i)
        answer += score
        visited.append(min_i)
        # print("-----------------------------")
        # for kkk in islands:
        #     print(kkk)
    return answer

def merge_and_count(islands, min_i, tmp):
    erase_island = islands[min_i]
    for index in range(len(erase_island)):
        if islands[0][index] > erase_island[index]:
            islands[0][index] = erase_island[index]
    islands[0][0] = 10000
    return tmp

sol = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
print(sol)