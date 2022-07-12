# (num, loacation, color) = (0,U,w), (1,D,y), (2,L,g), (3,R,b), (4,F,r), (5,B,o)

loc_color = dict()
loc_color["U"] = 0
loc_color["D"] = 1
loc_color["L"] = 2
loc_color["R"] = 3
loc_color["F"] = 4
loc_color["B"] = 5
# print(loc_color)

num_to_color = dict()
num_to_color[0] = "w"
num_to_color[1] = "y"
num_to_color[2] = "b"
num_to_color[3] = "g"
num_to_color[4] = "o"
num_to_color[5] = "r"

relation = [[50,51,52,32,31,30,42,41,40,20,21,22],[58,57,56,28,27,26,46,47,48,36,37,38],[0,3,6,40,43,46,16,13,10,56,53,50],[8,5,2,52,55,58,12,15,18,48,45,42],[6,7,8,30,33,36,18,17,16,26,24,20],[2,1,0,22,25,28,10,11,12,38,35,32]]

def rotate_own(location, direction):
    clock = [6,3,0,7,4,1,8,5,2]
    c_clock = [2,5,8,1,4,7,0,3,6]
    temp = [0 for _ in range(9)]
    for i in range(9):
        temp[i] = cube_list[10*loc_color[location] + i]
    if direction == "+":
        for j in range(9):
            cube_list[10*loc_color[location] + clock[i]] = temp[i]
    else:
        for j in range(9):
            cube_list[10*loc_color[location] + c_clock[i]] = temp[i]

def go_back_3(my_array, direction):
    if direction == "+":
        my_left = my_array[9:]
        my_right = my_array[:9]
        my_new = my_left + my_right
    else:
        my_left = my_array[3:]
        my_right = my_array[:3]
        my_new = my_left + my_right
    return my_new

def rotate_else(location, direction):
    original = relation[loc_color[location]]
    else_temp = [0 for _ in range(12)]
    for i in range(12):
        else_temp[i] = cube_list[original[i]]
    cur = go_back_3(original, direction)
    for j in range(12):
        cube_list[cur[j]] = else_temp[j]

t = int(input())
for test_case in range(t):
    cube_list = [-1 for _ in range(60)]
    for loca in range(6):
        for color in range(9):
            cube_list[10*loca + color] = loca

    times = int(input())
    rotate_list = list(map(str, input().split()))
    for each_rotate in rotate_list:
        my_loca = each_rotate[0]
        my_direc = each_rotate[1]
        rotate_own(my_loca, my_direc)
        rotate_else(my_loca, my_direc)
    answer_1 = []
    answer_2 = []
    answer_3 = []
    for go_ele_1 in cube_list[:3]:
        answer_1.append(num_to_color[go_ele_1])
    for go_ele_2 in cube_list[3:6]:
        answer_2.append(num_to_color[go_ele_2])
    for go_ele_3 in cube_list[6:9]:
        answer_3.append(num_to_color[go_ele_3])
    print(*answer_1)
    print(*answer_2)
    print(*answer_3)
    print("-------------")


    

