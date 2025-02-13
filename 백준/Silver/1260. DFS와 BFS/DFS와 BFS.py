# DFS와 BFS
from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N + 1):
    graph[i].sort()


def dfs(v):
    print(v, end=" ")
    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            dfs(next)


queue = deque()


def bfs(v):
    visited[v] = True
    queue.append(v)
    while queue:
        now = queue.popleft()
        print(now, end=" ")

        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)


dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)
