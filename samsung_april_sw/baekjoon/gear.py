gears = [[0]*8]
for _ in range(4):
    gear = list(map(int, input()))
    gears.append(gear)
gears.append([[0]*8])
k = int(input())
rotates = []
for _ in range(k):
    num, direction = map(int, input().split())
    rotates.append([num, direction])
# print(gears)
# print(rotates)

def rotate(gears, index, direction):
    if direction == 1:
        head = [gears[index].pop()]
        gears[index] = head + gears[index]
        return gears[index]
    else:
        tail = gears[index].pop(0)
        gears[index].append(tail)
        return gears[index]

def can_rotate(left, right):
    if left[2] != right[6]:
        return True
    return False

def left_rotate(gears, index, direction):
    rotate(gears, index, direction)
    if index == 0 or 5:
        return 0
    if can_rotate(gears[index-1], gears[index]) == True:
        left_rotate(gears, index-1, direction*-1)
def right_rotate(gears, index, direction):
    # print("cur index, direction", index, direction)
    rotate(gears, index, direction)
    if index == 0 or 5:
        return 0
    if can_rotate(gears[index], gears[index+1]) == True:
        right_rotate(gears, index+1, direction*-1)
for ele in rotates:
    rotate(gears, ele[0], -1*ele[1])
    left_rotate(gears, ele[0], ele[1])
    right_rotate(gears, ele[0], ele[1])

answer = 0
for ii in range(4):
    answer += gears[ii+1][0] * 2**(ii)
    print("gear", gears[ii+1])
print(answer)

# print("testtesttesttesttesttesttesttesttesttest")

# print(can_rotate(gears[3], gears[3+1]))
