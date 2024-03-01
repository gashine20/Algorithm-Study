import sys

input = sys.stdin.readline

n, m = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(sum(cost) + 1):
        if j >= cost[i - 1]:
            dp[i][j] = max(memory[i-1] + dp[i - 1][j - cost[i-1]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

answer = 0

# for i in dp:
#     print(i)

# flag = False
# for i in range(sum(cost) + 1):
#     for j in range(1, n + 1):
#         if dp[j][i] >= m:
#             flag=True
#             answer = i
#             break
#     if flag:
#         break

for i in range(len(dp[n])):
    if dp[n][i] >= m:
        answer = i
        break


print(answer)
