# 1로 만들기

N = int(input())

D = [0] * 1000001
D[1] = 0
D[2] = 1
D[3] = 1

for i in range(4, 1000001):
    D[i] = 1 + D[i - 1]

    if i % 2 == 0:
        D[i] = min(D[i], 1 + D[int(i / 2)])

    if i % 3 == 0:
        D[i] = min(D[i], 1 + D[int(i / 3)])

print(D[N])
