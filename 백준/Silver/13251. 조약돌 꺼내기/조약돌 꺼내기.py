# 조약돌 꺼내기

M = int(input())

color = list(map(int, input().split()))
K = int(input())

total = 0

totalChance = 0
pickChance = 0

for c in color:
    total += c

ans = 0
probability = [1] * 51

for i in range(M):
    if color[i] < K:
        continue

    for k in range(K):
        probability[i] = probability[i] * (color[i] - k) / (total - k)

    ans += probability[i]

print(ans)
