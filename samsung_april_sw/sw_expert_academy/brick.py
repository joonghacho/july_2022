import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def rotate(my_array):
    temp = zip(*my_array)
    new_array = [list(ele) for ele in temp]
    return new_array[::-1]

def get_init_brick(init_game_map, start_num):
    for brick_i in range(len(init_game_map[0])):
        if init_game_map[start_num][brick_i] != 0:
            return [brick_i, start_num, init_game_map[start_num][brick_i]]
    return "none"

# brick = [x, y, num_of_brick]
def boom(boom_game_map, brick):
    queue = [brick]
    while queue:
        cur_brick = queue.pop(0)
        boom_game_map[cur_brick[1]][cur_brick[0]] = 0
        if cur_brick[2] >= 2:
            for direction in range(4):
                for length in range(1, cur_brick[2]):
                    candi_x = cur_brick[0] + length * dx[direction]
                    candi_y = cur_brick[1] + length * dy[direction]
                    if 0 <= candi_x < h and 0 <= candi_y < w:
                        if boom_game_map[candi_y][candi_x] >= 2:
                            queue.append([candi_x, candi_y, boom_game_map[candi_y][candi_x]])
                        boom_game_map[candi_y][candi_x] = 0
    return

def go_right(right_game_map):
    new_game_map = []
    for one_line in right_game_map:
        cnt = 0
        non_zero = []
        for line_i in range(len(one_line)):
            if one_line[line_i] == 0:
                cnt += 1
            else:
                non_zero.append(one_line[line_i])
        one_line = [0 for _ in range(cnt)] + non_zero
        new_game_map.append(one_line)
    return new_game_map

def dfs(count, cur_map):
    global answer
    if count == n:
        answer_candidate = 0
        for jj in range(len(cur_map)):
            for ii in range(len(cur_map[0])):
                if cur_map[jj][ii] != 0:
                    answer_candidate += 1
        if answer > answer_candidate:
            answer = answer_candidate
            # print(answer, "answer")
            # for iiii in cur_map:
            #     print(iiii)
            # print("---------------")
        return
    for k in range(w):
        temp_map = copy.deepcopy(cur_map)
        init_brick = get_init_brick(cur_map, k)
        if init_brick == "none":
            continue
        boom(cur_map, init_brick)
        cur_map = go_right(cur_map)
        dfs(count + 1, cur_map)
        cur_map = temp_map

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        n, w, h = map(int, input().split())

        ori_map = []
        for _ in range(h):
            line = list(map(int, input().split()))
            ori_map.append(line)
        
        game_map = rotate(ori_map)
        # print("game_map:")
        # for kkkk in game_map:
            # print(kkkk)
        # print("----------------------------")
        answer = 300
        dfs(0, game_map)
        if answer == 300:
            print("#" + str(test_case) + " " + str(0))
        else:
            print("#" + str(test_case) + " " + str(answer))
