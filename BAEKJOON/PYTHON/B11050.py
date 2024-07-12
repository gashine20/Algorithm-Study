# 이항 계수 1

N, K = map(int, input().split())

D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# for i in range(0, N + 1):
#     for j in range(0, i + 1):
#         if j == 0 or i == j:
#             D[i][j] = 1

for i in range(0, N + 1):
    D[i][1] = i #추가
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, N + 1):
    for j in range(1, i):
        D[i][j] = D[i - 1][j - 1] + D[i - 1][j]

print(D[N][K])
