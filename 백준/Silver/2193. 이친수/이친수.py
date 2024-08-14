# 이친수

N = int(input())
D = [[0 for _ in range(2)] for _ in range(N + 1)]

if N >= 3:
    D[3][0] = 1
    D[3][1] = 1

    for i in range(4, N + 1):
        D[i][0] = D[i - 1][0] + D[i - 1][1]
        D[i][1] = D[i - 1][0]

result = 0

if N == 1 or N == 2:
    result = 1
else:
    result = D[N][0] + D[N][1]

print(result)
