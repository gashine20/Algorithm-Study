import sys

input = sys.stdin.readline

n, k = map(int, input().split())
c = [int(input()) for i in range(n)]

# 점화식?
dp = [0] * (k + 1)
dp[0] = 1

# dp 설정
for i in c:
    for j in range(i, k + 1):  # 1~10, 2~10, 5~10
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])
