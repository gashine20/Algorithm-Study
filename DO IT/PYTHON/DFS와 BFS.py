from collections import deque

N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)


for i in range(1, N+1):
    arr[i].sort()

# print(arr)
dfs_visited = []


def DFS(v):
    print(v, end=" ")
    dfs_visited.append(v)

    for a in arr[v]:
        if a not in dfs_visited:
            DFS(a)


DFS(V)
print()


def BFS(v):
    bfs_stack = deque()
    bfs_visited = []

    bfs_stack.append(v)
    bfs_visited.append(v)

    while bfs_stack:
        edge = bfs_stack.popleft()
        print(edge, end=" ")

        for a in arr[edge]:
            if a not in bfs_visited:
                bfs_visited.append(a)
                bfs_stack.append(a)


BFS(V)
