# 1890

n = int(input())
jump = [] * n

for _ in range(n):
    jump.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

# 초기 설정
move = jump[0][0]
dp[move][0] += 1  # 오른쪽
dp[0][move] += 1  # 아래


def printDP():
    for i in dp:
        print(i)
    print()


for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[n - 1][n - 1])  # 정답 출력
        else:
            move = jump[i][j]
            if i + move < n:
                dp[i + move][j] += dp[i][j]
            if j + move < n:
                dp[i][j + move] += dp[i][j]
        # printDP()
