import sys
t = int(input())
for i in range(t):
    n = int(input())
    answer = 0
    dices = list(map(int, sys.stdin.readline().split()))
    dices.sort()
    while dices:
        if answer < dices.pop(0):
            answer += 1
    print("Case #"+str(i+1)+":",answer)