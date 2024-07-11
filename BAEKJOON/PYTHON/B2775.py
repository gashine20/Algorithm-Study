# 부녀회장이 될 테야

floor = 14
D = [[0 for _ in range(floor + 1)] for _ in range(floor + 1)]

# i 층, j 호
for i in range(floor + 1):
    if i == 0:
        for j in range(1, floor + 1):
            D[i][j] = j
    else:
        D[i][1] = 1

for i in range(1, floor + 1):
    for j in range(2, floor + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(D[k][n])
