from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# 큐에 인접하면 계속 담아
def bfs(a, b):
    myqueue = deque()
    myqueue.append((a, b))
    graph[a][b] = 0  # graph 리스트 직접 수정
    count = 1

    while myqueue:
        x, y = myqueue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0  # graph 리스트 직접 수정
                    myqueue.append((nx, ny))
                    count += 1

    return count


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
building = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            building.append(bfs(i, j))
            # printMap()

print(len(building))

for b in building:
    print(b)
