import sys

input = sys.stdin.readline

# MCN 구하기 M개 중 N 선택
D = [[0 for _ in range(31)] for _ in range(31)]

for i in range(31):
    D[i][i] = 1
    D[i][0] = 1
    D[i][1] = i

for i in range(1, 31):
    for j in range(2, 31):
        D[i][j] = D[i - 1][j - 1] + D[i - 1][j]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(D[M][N])
