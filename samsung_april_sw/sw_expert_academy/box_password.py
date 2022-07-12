def rotate(box):
    element = box.pop()
    k = [element]
    return k + box

num_dict = dict()
for i in range(10):
    num_dict[str(i)] = i
for j in range(6):
    num_dict[chr(65+j)] = 10 + j
# print(num_dict)

def get_num(small_numbers):
    num_leng = len(small_numbers)
    num = 0 
    for length in range(num_leng):
        num += num_dict[small_numbers[length]] * (16**(num_leng-length-1))
    return num

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    # print(n, k)
    num_list = list(map(str, input()))
    # print(num_list)
    rotate_time = n//4
    candidates = []
    for _ in range(rotate_time):
        num_list = rotate(num_list)
        # print(num_list)
        for hi in range(4):
            candi = []
            for kk in range(rotate_time):
                candi.append(num_list[hi * rotate_time + kk])
            candidates.append(candi)
    # print(candidates)
    # set_candidates = set(candidates)
    candidates_10 = [get_num(candi_10) for candi_10 in candidates]
    # print(candidates_10)
    answer_list = list(set(candidates_10))
    answer_list.sort(reverse = True)
    # print(answer_list)
    # print(k)
    answer = answer_list[k-1]
    print("#" + str(test_case) + " " + str(answer))