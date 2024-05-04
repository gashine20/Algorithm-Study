# DFS와 BFS
# 깊이 탐색 - 재귀, 너비 탐색 - 큐, 선입선출

from collections import deque
import sys

sys.setrecursionlimit(10000)

N, M, V = map(int, input().split())

node = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
myque = deque()

for _ in range(M):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

    node[s].sort()
    node[e].sort()

def dfs(start):
    print(start, end=" ")
    visited[start] = True

    for next in node[start]:
        if not visited[next]:
            dfs(next)

def bfs(start):
    visited[start] = True
    myque.append(start)

    while myque:
        now = myque.popleft()
        print(now, end=" ")

        for next in node[now]:
            if not visited[next]:
                visited[next] = True
                myque.append(next)


dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)
