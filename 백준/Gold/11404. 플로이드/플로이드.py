import sys
# 플로이드-워셜 => O(v^3)

input = sys.stdin.readline

n = int(input())
m = int(input())

floyd = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    floyd[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, input().split())

    if cost < floyd[start][end]:
        floyd[start][end] = cost

for k in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if floyd[start][end] > floyd[start][k] + floyd[k][end]:
                floyd[start][end] = floyd[start][k] + floyd[k][end]

for i in range(1, n+1):
    for j in range(1, n+1):
        if floyd[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(floyd[i][j], end=" ")
    print()