n = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

max_answer = -10**9
min_answer = 10**9

def dfs(plus, minus, multiply, divide, depth, total):
    global max_answer
    global min_answer
    
    if depth == n:
        if total > max_answer:
            max_answer = total
        if total < min_answer:
            min_answer = total
        return 0
    if plus:
        dfs(plus - 1, minus, multiply, divide, depth + 1, total + num_list[depth])
    if minus:
        dfs(plus, minus - 1, multiply, divide, depth + 1, total - num_list[depth])
    if multiply:
        dfs(plus, minus, multiply - 1, divide, depth + 1, total * num_list[depth])
    if divide:
        dfs(plus, minus, multiply, divide - 1, depth + 1, int(total / num_list[depth]))

dfs(operator_list[0], operator_list[1], operator_list[2], operator_list[3], 1, num_list[0])
print(max_answer)
print(min_answer)
