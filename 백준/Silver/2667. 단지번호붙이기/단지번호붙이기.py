# 단지 번호 붙이기
from collections import deque

N = int(input())
board = [] * N
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    board.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    board[x][y] = 0
    queue.append((x, y))
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    queue.append((nx, ny))

    return count


result = 0
home = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            result += 1
            home.append(bfs(i, j))

print(result)
home.sort()
for h in home:
    print(h)
