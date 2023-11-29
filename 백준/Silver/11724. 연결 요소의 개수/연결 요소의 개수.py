# DFS
import sys
sys.setrecursionlimit(10**6) # 추가
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


def DFS(v):
    visited[v] = True
    for a in arr[v]:
        if not visited[a]:
            DFS(a)


for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
#print(arr)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        count += 1

print(count)
