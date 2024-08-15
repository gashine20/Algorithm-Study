# 게임

N, M = map(int, input().split())

board = [] * N
visited = [[False for _ in range(M)] for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(str, input())))

move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# def is_holeAndOut(nx, ny):
#     if nx < 0 or nx >= M or ny < 0 or ny >= N:  # 범위 넘으면
#         return True
#     else:
#         if board[ny][nx] == "H":  # "H"에 도착하면
#             return True
#
#     return False


def moving(x, y):

    visited[y][x] = True
    max_moves = 0

    for dx, dy in move:
        nx = x + (dx * int(board[y][x]))
        ny = y + (dy * int(board[y][x]))

        # if not is_holeAndOut(nx, ny) and not visited[ny][nx]:  # 범위를 벗어나지 않으면
        #     moving(nx, ny, count + 1)
        #     print("nx=", nx, "ny=", ny, "count=", count + 1)

        if nx >= 0 and nx < M and ny >= 0 and ny < N and board[ny][nx] != 'H':
            if visited[ny][nx]:
                print(-1)
                exit()
            max_moves = max(max_moves, moving(nx, ny))

        visited[y][x] = False
        dp[y][x] = max_moves + 1
        return dp[y][x]


print(moving(0, 0))
