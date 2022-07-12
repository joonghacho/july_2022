import copy
import sys
# sys.setrecursionlimit(100000000)

def rotate(rotate_film):
    temp = zip(*rotate_film[::-1])
    return [list(ele) for ele in temp]

def rotate_reverse(reverse_film):
    reverse_film = zip(*reverse_film)
    return [list(ele_r) for ele_r in reverse_film][::-1]

def check_pass(check_film):
    check_list = []
    for check_ele in check_film:
        cnt_list = []
        cnt = 1
        for cell_i in range(len(check_ele)):
            if cell_i == len(check_ele)-1:
                cnt_list.append(cnt)
            else:
                if check_ele[cell_i] == check_ele[cell_i + 1]:
                   cnt += 1
                else:
                    cnt_list.append(cnt)
                    cnt = 1
        # print(cnt_list,"cnt_list")
        if max(cnt_list) >= k:
            check_list.append(1)
        else:
            check_list.append(0)
    # print(sum(check_list))
    if sum(check_list) == len(check_film):
        return True
    return False

def coloring(color, line_num, color_film):
    temp_color_film = rotate_reverse(color_film)
    for color_ele in range(len(temp_color_film[line_num])):
        temp_color_film[line_num][color_ele] = color
    answer_color_film = rotate(temp_color_film)
    return answer_color_film

def dfs(count, dfs_film):
    global answer
    if count >= k:
        return
    if check_pass(dfs_film) == True:
        if answer > count:
            print("dfs_film")
            for kkkk in dfs_film:
                print(kkkk)
            print("--------")
            answer =count
        return
    for my_line in range(h*2):
        my_temp_film = copy.deepcopy(dfs_film)
        coloring(my_line//h, my_line%h, dfs_film)
        dfs(count + 1, dfs_film)
        dfs_film = my_temp_film

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        h, w, k = map(int, input().split())
        film = []
        for _ in range(h):
            line = list(map(int, input().split()))
            film.append(line)
        film = rotate(film)
        answer = k
        if check_pass(film) == True:
            print("#" + str(test_case) + " " + str(0))
        else:
            dfs(0, film)
            print("#" + str(test_case) + " " + str(answer))
        # for kkkk in film:
        #     print(kkkk)
        # print(check_pass(film))
        # newnew = coloring(1, 2, film)
        # for iii in newnew:
        #     print(iii)

