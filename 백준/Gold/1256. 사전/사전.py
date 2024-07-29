# 사전

N, M, K = map(int, input().split())

# (N+M) C (K) = 사전에 수록되어 있는 문자열 개수

D = [[0 for _ in range(N + M + 1)] for _ in range(N + M + 1)]

for i in range(N + M + 1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(1, N + M + 1):
    for j in range(1, N + M + 1):
        D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

T = D[N + M][M]  # 모든 경우의 수

if T < K:
    print("-1")
else:
    while not (N == 0 and M == 0):
        if D[N - 1 + M][M] >= K:
            print("a", end="")
            N -= 1
        else:
            print("z", end="")
            K -= D[N - 1 + M][M]
            M -= 1
