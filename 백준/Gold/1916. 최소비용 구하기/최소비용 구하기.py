# 최소비용 구하기
import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

graph = [[] for _ in range(N + 1)]
distance = [sys.maxsize] * (N + 1)
visited = [False] * (N + 1)
myqueue = PriorityQueue()

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())  # 출발 도시, 도착 도시


def dikstra(s):
    distance[s] = 0
    myqueue.put((0, s))

    while myqueue.qsize() > 0:
        now = myqueue.get()
        now_node = now[1]

        if visited[now_node]:
            continue

        visited[now_node] = True
        for next, weight in graph[now_node]:
            if visited[next]:
                continue

            if distance[next] > distance[now_node] + weight:
                distance[next] = distance[now_node] + weight
                myqueue.put((distance[next], next))


dikstra(start)
print(distance[end])
