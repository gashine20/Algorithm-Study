# 미로 탐색
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

miro = [[] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    miro[i] = list(map(int, input().strip()))


def bfs(x, y, point):
    myque = deque()
    myque.append((x, y, point))
    visited[x][y] = True

    while myque:
        nx, ny, npoint = myque.popleft()
        miro[nx][ny] = npoint

        for i in range(4):
            next_x = nx + dx[i]
            next_y = ny + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if miro[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    myque.append((next_x, next_y, npoint + 1))


bfs(0, 0, 1)
print(miro[N - 1][M - 1])
