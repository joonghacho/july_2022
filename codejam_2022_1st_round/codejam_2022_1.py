def get_result(row, col):
    for j in range(row*2 + 1):
        answer_row = ""
        for i in range(col*2 + 1):
            if j < 2 and i < 2:
                answer_row += "."
            elif j % 2 == 0 and i % 2 == 0:
                answer_row += "+"
            elif j % 2 == 1 and i % 2 == 0:
                answer_row += "|"
            elif j % 2 == 0 and i % 2 == 1:
                answer_row += "-"
            elif j % 2 == 1 and i % 2 == 1:
                answer_row += "."
        print(answer_row)

t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    print("Case #"+str(i+1)+":")
    get_result(r, c)