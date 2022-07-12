def solution(lottos, win_nums):
    answer = []
    same_num = 0
    zero_num = 0
    for candi in lottos:
        if candi in win_nums:
            same_num += 1
        if candi == 0:
            zero_num += 1
    max_num = same_num + zero_num
    min_num = same_num

    for i in range(1, 6):
        if max_num == 7 - i:
            answer.append(i)
    if len(answer) == 0:
        answer.append(6)
    for i in range(1, 6):
        if min_num == 7 - i:
            answer.append(i)
    if len(answer) == 1:
        answer.append(6)

    return answer