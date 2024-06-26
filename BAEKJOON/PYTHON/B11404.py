# 플로이드
# 가장 빠른 버스 노선 구하기
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

cost = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):  # 같은 i, j 0으로 초기화
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if cost[a][b] > c:
        cost[a][b] = c

for k in range(1, n + 1):  # 경유지
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            cost[s][e] = min(cost[s][e], cost[s][k] + cost[k][e])

            # if cost[s][e] > cost[s][k] + cost[k][e]:
            #     cost[s][e] = cost[s][k] + cost[k][e]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(cost[i][j], end=" ")
    print()
