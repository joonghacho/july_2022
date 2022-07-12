n, m = map(int, input().split())
my_map = []
for _ in range(n):
    line = list(map(int, input().split()))
    my_map.append(line)

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def shape_1(my_map):
    row = len(my_map)
    col = len(my_map[0])
    answer = []
    for j in range(row):
        for i in range(col - 3):
            candi = my_map[j][i] + my_map[j][i+1] + my_map[j][i+2] + my_map[j][i+3]
            answer.append(candi)
    return max(answer)

def shape_2(my_map):
    row = len(my_map)
    col = len(my_map[0])
    answer = []
    for j in range(row-1):
        for i in range(col - 1):
            candi = my_map[j][i] + my_map[j][i+1] + my_map[j+1][i] + my_map[j+1][i+1]
            answer.append(candi)
    return max(answer)

def shape_3(my_map):
    row = len(my_map)
    col = len(my_map[0])
    answer = []
    for j in range(row-2):
        for i in range(col - 1):
            candi = my_map[j][i] + my_map[j+1][i] + my_map[j+2][i] + my_map[j+2][i+1]
            answer.append(candi)
    return max(answer)

def shape_4(my_map):
    row = len(my_map)
    col = len(my_map[0])
    answer = []
    for j in range(row-1):
        for i in range(col - 2):
            candi = my_map[j][i] + my_map[j][i+1] + my_map[j][i+2] + my_map[j+1][i+2]
            answer.append(candi)
    return max(answer)

def shape_5(my_map):
    row = len(my_map)
    col = len(my_map[0])
    answer = []
    for j in range(row-2):
        for i in range(col - 1):
            candi = my_map[j][i] + my_map[j+1][i] + my_map[j+1][i+1] + my_map[j+2][i+1]
            answer.append(candi)
    return max(answer)

def shape_6(my_map):
    row = len(my_map)
    col = len(my_map[0])
    answer = []
    for j in range(row-1):
        for i in range(col - 2):
            candi = my_map[j][i] + my_map[j][i+1] + my_map[j+1][i+1] + my_map[j+1][i+2]
            answer.append(candi)
    return max(answer)

def shape_7(my_map):
    row = len(my_map)
    col = len(my_map[0])
    answer = []
    for j in range(row-1):
        for i in range(col - 2):
            candi = my_map[j][i] + my_map[j][i+1] + my_map[j][i+2] + my_map[j+1][i+1]
            answer.append(candi)
    return max(answer)

last_candi = []
for _ in range(4):
    real_answer = []
    my_map = rotated(my_map)
    # for kk in my_map:
    #     print(kk)
    real_answer.append(shape_1(my_map))
    real_answer.append(shape_2(my_map))
    real_answer.append(shape_3(my_map))
    real_answer.append(shape_4(my_map))
    real_answer.append(shape_5(my_map))
    real_answer.append(shape_6(my_map))
    real_answer.append(shape_7(my_map))
    last_candi.append(max(real_answer))
    
last_answer = max(last_candi)
print(last_answer)