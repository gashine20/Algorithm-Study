import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = [] * (N + 1)

for _ in range(N):
    coin.append(int(input()))

count = 0
for i in range(N - 1, -1, -1):
    if K >= coin[i]:
        count += int(K / coin[i])
        K = K % coin[i]

print(count)
