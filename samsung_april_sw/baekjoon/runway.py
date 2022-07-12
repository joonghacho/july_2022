n, l = map(int, input().split())
my_map = []
for _ in range(n):
    one_line = list(map(int, input().split()))
    my_map.append(one_line)
# print(my_map)
def check_go(way, l, i, made_ele):
    if i+l-1 <= n-1:
        for run in range(l):
            if way[i+run] != way[i]:
                return False
        for runrun in range(l):
            made_ele.append(n-1-(i+runrun))
        return True
    return False

def can_go(way):
    made = []
    for i in range(n-1):
        if abs(way[i] - way[i+1]) != 0 and abs(way[i] - way[i+1]) != 1:
            return False
    for i in range(n-1):
        if way[i] - way[i+1] == 1:
            if check_go(way, l, i+1, made) == False:
                return False
    reverse_way = list(reversed(way))
    for i in range(n-1):
        if reverse_way[i] - reverse_way[i+1] == 1:
            for run in range(l):
                if i+1+run in made:
                    return False
            if check_go(reverse_way, l, i+1, made) == False:
                return False
    return True

# for kk in my_map:
#     print(can_go(kk))
answer = 0
for ori in my_map:
    # print(ori)
    # print(can_go(ori))
    if can_go(ori) == True:
        answer += 1

# print("asdf;lkja;lfjasflkjsadfl;jas")
temp = zip(*my_map[::-1])
rotate_map = list(list(ele) for ele in temp)
# for kkk in rotate_map:
#     print(kkk)
# print("skfjhaskfhalskfjh")
for new in rotate_map:
    # print(new)
    # print(can_go(new))
    if can_go(new) == True:
        answer += 1

print(answer)
