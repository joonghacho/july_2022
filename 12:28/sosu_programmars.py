from itertools import combinations
def is_sosu(n):
    for i in range(2, int(n**0.5 +2)):
        if n % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for candi in combi:
        sum_candi = sum(candi)
        answer += is_sosu(sum_candi)
    return answer

sol = solution([1,2,7,6,4])