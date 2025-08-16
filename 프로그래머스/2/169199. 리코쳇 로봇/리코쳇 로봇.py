from collections import deque
import sys

def solution(board):
    n, m = len(board), len(board[0])
    robot, goal = None, None

    # G, R 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                robot = (i, j)
            if board[i][j] == "G":
                goal = (i, j)
    
    # visited 초기화
    visited = [[sys.maxsize for _ in range(m)] for _ in range(n)]
    visited[robot[0]][robot[1]] = 0
    
    
    def find_next(x, y, dx, dy):
        # dx: 0, dy: 1, pos: 현재 위치
        while True:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "D":
                x, y = nx, ny
            else:
                break
        
        return x, y
        
            
    def bfs(start):        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        queue = deque()
        x, y = start
        queue.append((x, y, 0))
        
        while queue:
            x, y, m = queue.popleft()
            
            if (x, y) == goal:
                return m
            
            for i in range(4):
                nx, ny = find_next(x, y, dx[i], dy[i])
                if visited[nx][ny] > m + 1:
                    queue.append((nx, ny, m + 1))
                    visited[nx][ny] = m + 1
                    
        return -1
    
    answer = bfs(robot)
    return answer