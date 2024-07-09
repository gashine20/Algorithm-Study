# 다리 놓기

site = 30
D = [[0 for _ in range(site + 1)] for _ in range(site + 1)]

for i in range(site + 1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(1, site + 1):
    for j in range(2, i):
        D[i][j] = D[i - 1][j - 1] + D[i - 1][j]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(D[M][N])
