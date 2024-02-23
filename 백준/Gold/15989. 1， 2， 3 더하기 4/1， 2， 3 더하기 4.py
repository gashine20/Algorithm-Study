T = int(input())

testcase = [] * T
for _ in range(T):
    testcase.append(int(input()))

dp = [1] * 10001
for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for t in testcase:  # 4,7,10
    print(dp[t])
