from collections import deque


# 시작, 레버, 탈출 위치 찾기
def find_position(maps):
    positions = {'S': [], 'E': [], 'L': []}

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] in positions:
                positions[maps[i][j]].append((j, i))

    return positions


def bfs(start, end, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    l = len(maps)  # 세로
    w = len(maps[0])  # 가로
    visited = [[False for _ in range(w)] for _ in range(l)]
    d = deque()

    d.append((start[0][0], start[0][1], 0))

    while d:
        x, y, cnt = d.popleft()
        
        if x == end[0][0] and y == end[0][1]:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < l and maps[ny][nx] != 'X':
                if not visited[ny][nx]:  # 방문하지 않았으면
                    d.append((nx, ny, cnt + 1))
                    visited[ny][nx] = True

    return -1  # 갈 수 없으면


def solution(maps):
    answer = -1
    positions = find_position(maps)

    path1 = bfs(positions['S'], positions['L'], maps)  # start -> lever
    path2 = bfs(positions['L'], positions['E'], maps)  # lever-> exit
    if path1 != -1 and path2 != -1:
        answer = path1 + path2

    return answer
