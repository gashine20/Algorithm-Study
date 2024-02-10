N, M = map(int, input().split())

graph = [] * (N + 1)
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        # 방문한 노드는 1로 만들고, 인접 노드들 돈 다음에 return True
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i, j):
            result += 1

print(result)
