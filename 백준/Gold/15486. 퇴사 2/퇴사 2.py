# 퇴사2
import sys

input = sys.stdin.readline

n = int(input())
T = [] * (n + 1)
P = [] * (n + 1)
D = [0 for _ in range(n + 1)]

T.append(0)
P.append(0)

for i in range(1, n + 1):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

result = 0

for i in range(1, n + 1):
    D[i] = max(D[i], D[i - 1])
    pos = i + T[i] - 1
    if pos <= n:
        D[pos] = max(D[pos], D[i - 1] + P[i])

print(max(D))
