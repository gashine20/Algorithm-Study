import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))  # 방향 있음 유의!

start, end = map(int, input().split())
# print(graph)

distance = [sys.maxsize] * (N + 1)
queue = PriorityQueue()

queue.put((0, start))
distance[start] = 0

while queue.qsize() > 0:
    current = queue.get()

    current_node = current[1]

    if visited[current_node]:
        continue

    visited[current_node] = True

    for tmp in graph[current_node]:
        next = tmp[0]  # 노드
        value = tmp[1]  # 거리

        if visited[next]:
            continue

        if distance[next] > distance[current_node] + value:
            distance[next] = distance[current_node] + value

            queue.put((distance[next], next))

            # print("current_node:", current_node, "next:", next, distance)

print(distance[end])
