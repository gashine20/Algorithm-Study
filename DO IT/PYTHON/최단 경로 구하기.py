# 다익스트라
import sys
from queue import PriorityQueue
input = sys.stdin.readline

# V(정점의 개수), E(간선의 개수)
V, E = map(int, input().split())
# K (시작 정점)
K = int(input())

direction = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
queue = PriorityQueue()
distance = [sys.maxsize] * (V + 1)

for _ in range(E):
    start, end, weight = map(int, input().split())

    direction[start].append([end, weight])

# print("direction", direction)

queue.put((0, K))  # K를 시작점으로 (거리, 출발)
distance[K] = 0

while queue.qsize() > 0:
    current = queue.get()

    current_node = current[1]

    if visited[current_node]:
        continue

    visited[current_node] = True

    for tmp in direction[current_node]:
        next = tmp[0]
        value = tmp[1]

        if visited[next]:
            continue

        if distance[next] > distance[current_node] + value:  # 더 짧은 distance 갱신
            distance[next] = distance[current_node] + value

            queue.put((distance[next], next))

for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
