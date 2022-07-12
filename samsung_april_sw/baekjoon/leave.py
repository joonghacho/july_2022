n = int(input())

my_list = []
for i in range(n):
    one_day = []
    t, p = map(int, input().split())
    one_day.append(i + t -1)
    one_day.append(p)
    my_list.append(one_day)
# print(my_list)

dp = [0] * n
for j in range(n):
    for candi_i in range(len(my_list)):
        if my_list[candi_i][0] <= j:
            dp_candi = dp[candi_i - 1] + my_list[candi_i][1]
            if dp_candi > dp[j]:
                dp[j] = dp_candi

print(dp[-1])


