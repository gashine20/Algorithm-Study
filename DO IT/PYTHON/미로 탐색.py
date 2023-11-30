from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split(" "))
# A: 데이터 저장 2차원 행렬
# visited: 방문 기록 저장 리스트

maze = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    numbers = list(input())
    for j in range(M):
        maze[i][j] = int(numbers[j])


def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()
        # 상하좌우 확인
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]

            if 0 <= x < N and 0 <= y < M:
                if maze[x][y] != 0 and not visited[x][y]:
                    # visited, queue 추가
                    visited[x][y] = True
                    queue.append((x, y))
                    maze[x][y] = maze[now[0]][now[1]] + 1


BFS(0, 0)
print(maze[N - 1][M - 1])
