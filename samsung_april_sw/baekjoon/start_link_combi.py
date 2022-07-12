from itertools import combinations
from itertools import permutations

def get_score(ele):
    ele_combi = list(permutations(ele, 2))
    answer = 0
    for combi in ele_combi:
        answer += my_map[combi[0]][combi[1]]
    return answer

n = int(input())
my_map = []
for _ in range(n):
    line = list(map(int, input().split()))
    my_map.append(line)
# print(my_map)
people = [i for i in range(n)]
# print(people)
answer = 4000

start_candi = list(combinations(people, n//2))
link_candi = []
for start_ele in start_candi:
    link_ele = []
    for i in range(n):
        if i not in start_ele:
            link_ele.append(i)
    link_candi.append(tuple(link_ele))

for kk in range(len(start_candi)):
    one_start = get_score(start_candi[kk])
    one_link = get_score(link_candi[kk])
    answer_candidate = abs(one_start - one_link)
    if answer_candidate < answer:
        answer = answer_candidate

print(answer)