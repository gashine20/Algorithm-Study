# 연산자 끼워넣기
# + - x / 순서

N = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)

    if plus:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / numbers[depth]), plus, minus, multiply, divide - 1)


dfs(1, numbers[0], oper[0], oper[1], oper[2], oper[3])

print(maximum)
print(minimum)
