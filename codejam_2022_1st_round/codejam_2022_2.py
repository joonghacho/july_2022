def get_answer(da, db, dc):
    candidates = []
    for i in range(4):
        candi = min(da[i], db[i], dc[i])
        candidates.append(candi)
    if sum(candidates) < 1000000:
        return "IMPOSSIBLE"
    else:
        cat = 1000000
        answer_list = ["0", "0", "0", "0"]
        for ii in range(4):
            mine = candidates[ii]
            cat -= mine
            if cat >= 0:
                answer_list[ii] = str(mine)
            else:
                answer_list[ii] = str(mine+cat)
                break
        return ' '.join(answer_list)

t = int(input())
for i in range(t):
    da = list(map(int, input().split()))
    db = list(map(int, input().split()))
    dc = list(map(int, input().split()))
    print("Case #"+str(i+1)+":", get_answer(da, db, dc))