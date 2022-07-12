import sys

n = int(input())
test_rooms = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for i in range(n):
    test_rooms[i] -= b
# print(test_rooms)
answer += n
for room in test_rooms:
    if room > 0:
        answer += (room // c)
        if (room // c) * c != room:
            answer += 1
print(answer)