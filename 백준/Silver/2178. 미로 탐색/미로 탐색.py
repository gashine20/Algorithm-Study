import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

A = [[] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    A[i] = list(map(int, input().strip()))

myqueue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def printA():
    for i in A:
        print(i)
    print()


def bfs(a, b):
    myqueue.append((a, b))
    visited[a][b] = True

    while myqueue:
        x, y = myqueue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if A[nx][ny] != 0 and visited[nx][ny] == False:
                    A[nx][ny] = A[x][y] + 1
                    visited[nx][ny] = True
                    myqueue.append((nx, ny))

    #printA()

bfs(0, 0)
print(A[n - 1][m - 1])
