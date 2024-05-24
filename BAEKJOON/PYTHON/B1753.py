# 최단경로
from queue import PriorityQueue
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
startNode = int(input())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
distance = [sys.maxsize] * (V + 1)
myque = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    myque.put((0, start))  # 거리와 출발 노드 저장
    distance[start] = 0  # 시작노드 거리 0 초기화

    while myque.qsize() > 0:
        now = myque.get()
        now_node = now[1]
        print(list(myque.queue))
        print("now_node:", now_node, "weight:", now[1])
        if visited[now_node]:
            continue

        visited[now_node] = True

        for next, weight in graph[now_node]:
            if not visited[next]:
                if distance[next] > distance[now_node] + weight:
                    distance[next] = distance[now_node] + weight

                myque.put((distance[next], next))
        print(distance)


dijkstra(startNode)

for i in range(1, V + 1):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(distance[i])
