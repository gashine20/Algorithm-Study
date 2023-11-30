# DFS: 한 방향으로 갈 수 있을때까지 계속 가다가, 더이상 길이 없으면 가장 짧은 거리로 다시 돌아가 다른 방향으로 이동!
# 예시 추가
# 6 5 1
# 1 2
# 2 3
# 3 4
# 2 5
# 5 6
from collections import deque

N, M, V = map(int, input().split())
# A 그래프 데이터 저장 인접 리스트
A = [[] for _ in range(N + 1)]
visited = []

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

# 정렬
for i in range(1, len(A)):
    A[i].sort()


def DFS(v):  # 인자: 시작 edge
    print(v, end=" ")
    visited.append(v)
    for node in A[v]:
        if node not in visited:
            DFS(node)


DFS(V)
print()

# BFS : 너비 우선 탐색,
# : 루트노드에서 인접한 노드 먼저 탐색, 재귀적x, 큐FIFO, 더이상 방문할 곳 없으면 탐색마침
visited = [False] * (N + 1)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=" ")
        for node in A[now_Node]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


BFS(V)
