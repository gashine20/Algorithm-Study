# 다익스트라
import sys
import heapq  # 우선순위 큐

input = sys.stdin.readline

n, m, k = map(int, input().split())

direction = [[] for _ in range(n + 1)]
distance = [[sys.maxsize] * k for _ in range(n + 1)]

for _ in range(m):
    start, end, time = map(int, input().split())

    direction[start].append([end, time])

# print(direction)
distance[1][0] = 0
#print(distance)
pq = [(0, 1)]

while pq:
    cost, node = heapq.heappop(pq)

    for nextNode, nextCost in direction[node]:
        sumCost = cost + nextCost

        if distance[nextNode][k - 1] > sumCost:
            distance[nextNode][k - 1] = sumCost
            distance[nextNode].sort()

            heapq.heappush(pq, [sumCost, nextNode])


for dis in distance[1:]:
    if dis[k-1] == sys.maxsize:
        print(-1)
    else:
        print(dis[k-1])