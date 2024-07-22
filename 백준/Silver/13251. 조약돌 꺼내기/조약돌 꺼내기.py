# 조약돌 꺼내기

M = int(input())

color = list(map(int, input().split()))
K = int(input())

total = 0

totalChance = 0
pickChance = 0

for c in color:
    total += c

for i in range(M):
    C = color[i]
    if C < K:
        continue

    T = [[0 for _ in range(C + 1)] for _ in range(C + 1)]
    for i in range(C + 1):
        T[i][0] = 1
        T[i][i] = 1
        T[i][1] = i

    for i in range(1, C + 1):
        for j in range(1, C + 1):
            T[i][j] = T[i - 1][j] + T[i - 1][j - 1]

    # for t in T:
    #     print(t)

    pickChance += T[C][K]

# 전체 경우의 수
T = [[0 for _ in range(total + 1)] for _ in range(total + 1)]
for i in range(total + 1):
    T[i][0] = 1
    T[i][i] = 1
    T[i][1] = i

for i in range(1, total + 1):
    for j in range(1, total + 1):
        T[i][j] = T[i - 1][j] + T[i - 1][j - 1]

totalChance = T[total][K]

result = pickChance / totalChance
print(result)
