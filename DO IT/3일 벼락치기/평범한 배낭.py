import sys

input = sys.stdin.readline

n, k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

print(bag)
for i in range(1, n + 1):
    for w in range(1, k + 1):
        if w >= bag[i - 1][0]:  # "현재 최대무게 j가 해당 물건무게보다 큰 경우
            # 표의 윗 셀의 값과 현재 물건의 v + 이전 물건의 v 값의 최대값을 저장
            dp[i][w] = max(bag[i - 1][1] + dp[i - 1][w - bag[i - 1][0]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[n][k])
