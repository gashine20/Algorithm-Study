# 11724 연결 요소의 개
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

node = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)


# dfs - 깊이 탐색
def dfs(start):
    visited[start] = True
    for next in node[start]:
        if not visited[next]:
            dfs(next)


answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
