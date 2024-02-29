import sys

input = sys.stdin.readline

N, K = map(int, input().split())

D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    D[i][i] = 1
    D[i][0] = 1

for i in range(1, N + 1):
    for j in range(1, i):
        D[i][j] = D[i - 1][j - 1] + D[i - 1][j]

print(D[N][K])
