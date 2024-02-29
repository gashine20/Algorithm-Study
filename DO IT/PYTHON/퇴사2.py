# dp 의미를 뭐로 두어야 할지 모르겠다..
import sys

input = sys.stdin.readline

n = int(input())
schedule = [] * (n + 1)

schedule.append([0, 0])
for _ in range(n):
    schedule.append(list(map(int, input().split())))

#print(schedule)
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값
    fin_date = i + schedule[i][0] - 1
    if fin_date <= n:  # 최종일 안에 일이 끈나는 경우
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다...
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + schedule[i][1])
    # print(fin_date, dp)
print(max(dp))
