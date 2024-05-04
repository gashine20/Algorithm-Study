# ABCDE
import sys

sys.setrecursionlimit(10000)

N, M = map(int, input().split())

visited = [False] * N
friend = [[] for _ in range(N)]
level = 1

for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)


def dfs(start, level):
    if level == 5:
        return True
    # print("Start:", start, "level:", level)
    visited[start] = True

    for next in friend[start]:
        if not visited[next]:
            if dfs(next, level + 1):
                return True

    visited[start] = False  # 초기화


answer = 0
for i in range(N):
    if dfs(i, 1):
        answer = 1

print(answer)
