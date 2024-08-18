# 쉬운 계단 수

N = int(input())
mod = 1000000000

# dp[N][H] 길이가 N인 계단에서 H 높이로 종료되는 계단 수를 만들 수 있는 경우 수
dp = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]

    for j in range(1, 9):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod

result = 0

for i in range(10):
    result = ( result + dp[N][i] ) % mod

print(result)
