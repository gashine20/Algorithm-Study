# 체스판 다시 칠하기

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input())

result = N * M

for a in range(N - 8 + 1):
    for b in range(M - 8 + 1):
        w_index = 0
        b_index = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if board[i][j] != 'W':
                        b_index += 1
                    else:
                        w_index += 1
        min_value = min(b_index, w_index)
        result = min(result, min_value)

print(result)
