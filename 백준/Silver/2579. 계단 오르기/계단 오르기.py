# 계단 오르기

n = int(input())
stair = [int(input()) for _ in range(n)]

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0] + stair[1])
else:
    D = [0] * n
    D[0] = stair[0]
    D[1] = stair[0] + stair[1]
    D[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3, n):
        D[i] = max(D[i - 2] + stair[i], D[i - 3] + stair[i - 1] + stair[i])

    print(D[n - 1])
