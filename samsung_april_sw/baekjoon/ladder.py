import copy

n, m, h = map(int, input().split())
lines = []
my_map = [[] for _ in range(h)]
for _ in range(m):
    y, x = map(int, input().split())
    lines.append([x-1, y-1])
for ori_line in lines:
    my_map[ori_line[1]].append(ori_line[0])

def get_valid(cur_map):
    test_map = copy.deepcopy(cur_map)
    for j in range(h):
        for i in range(len(test_map[j])):
            test_map[j].append(test_map[j][i] - 1)
            test_map[j].append(test_map[j][i] + 1)
    candidate = [[] for _ in range(h)]
    for k in range(h):
        for l in range(n-1):
            if l not in test_map[k]:
                candidate[k].append(l)
    return candidate
print(my_map)
print(get_valid(my_map),"get_valid")
# print(my_map)

def check_is_num_even(check_map):
    is_num_even = []
    for num in range(n-1):
        cnt = 0
        for numbers in check_map:
            if num in numbers:
                cnt += 1
        is_num_even.append(cnt%2)
    return sum(is_num_even)

def get_answer(answer_map):
    get_1_valid = get_valid(answer_map)
    for jj in range(len(get_1_valid)):
        for ii in range(len(get_1_valid[jj])):
            test_1_map = copy.deepcopy(answer_map)
            test_1_map[jj].append(get_1_valid[jj][ii])
            if check_is_num_even(test_1_map) == 0:
                print(1)
                return

# print(is_num_even)
print(check_is_num_even(my_map), "print_Check")
if check_is_num_even(my_map) > 3:
    print(-1)
else:
    get_answer(my_map)



