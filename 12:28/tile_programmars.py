def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(n-2):
        dp[i+3] = dp[i+2] + dp[i+1]
    
    return dp[-1] % 1000000007

for i in range(20):
    sol = solution(i+2)
    print(sol)