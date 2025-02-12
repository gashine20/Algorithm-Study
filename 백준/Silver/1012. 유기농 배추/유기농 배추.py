# 유기농 배추
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0


def bfs(start, count):
    queue = deque()
    x = start[0]
    y = start[1]

    if Board[x][y] == 1:
        count += 1
        Board[x][y] = 0
        queue.append(start)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if Board[nx][ny] == 1:
                    Board[nx][ny] = 0
                    queue.append((nx, ny))
    return count


for _ in range(T):
    M, N, K = map(int, input().split())
    Board = [[0 for _ in range(N)] for _ in range(M)]
    F = []
    for _ in range(K):
        X, Y = map(int, input().split())
        F.append((X, Y))
        Board[X][Y] = 1

    result = 0

    for f in F:
        result = bfs(f, result)

    print(result)
