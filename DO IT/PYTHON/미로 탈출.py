from collections import deque

n, m = map(int, input().split())

graph = [] * n
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    myqueue = deque()
    myqueue.append((x, y))

    while myqueue:
        x, y = myqueue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if 0 <= nx < n and 0 <= ny < m:  # 범위 확인
                if graph[nx][ny] == 0:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    myqueue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
