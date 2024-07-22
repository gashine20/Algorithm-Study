# 조약돌 꺼내기

M = int(input())

color = list(map(int, input().split()))
K = int(input())

total = 0

for c in color:
    total += c

T = [[0 for _ in range(M + 1)] for _ in range(M + 1)]
for i in range(M + 1):
    T[i][0] = 1
    T[i][i] = 1
    T[i][1] = i

for i in range(1, M):
    for j in range(1, M):
        T[i][j] = T[i - 1][j] + T[i - 1][j - 1]

for t in T:
    print(t)

totalChance = T[total][K]
pickChance = 0

for c in color:
    pickChance += T[c][K]

result = pickChance / totalChance
