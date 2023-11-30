# 원래 규칙대로 잘 있으면 0
# 바꿔야 한다면 1

N, M = map(int, input().split())

chess = []

for _ in range(N):
    chess.append(list(input()))

# 있어야 할 자리에 없으면 1
result = []

for i in range(N - 7):
    for j in range(M - 7):
        W_index = 0  # 흰색으로 시작
        B_index = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: # 짝수 일때
                    if chess[a][b] != 'W': # B이면
                        W_index += 1
                    elif chess[a][b] != 'B': # W이면
                        B_index += 1
                else:  # 홀수 일 때
                    if chess[a][b] != 'B':
                        W_index += 1
                    elif chess[a][b] != 'W':
                        B_index += 1
        #print("W: ", W_index,"B: ", B_index )
        result.append(W_index)
        result.append(B_index)

print(min(result))

# 오답...
# if chess[0][0] == 'W':
#     for i in range(N):
#         for j in range(M):
#             if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
#                 if chess[i][j] != 'W':
#                     check_chess[i][j] = 1
#             else:
#                 if chess[i][j] != 'B':
#                     check_chess[i][j] = 1
# else:  # 시작이 B인 경우
#     for i in range(N):
#         for j in range(M):
#             if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
#                 if chess[i][j] != 'B':
#                     check_chess[i][j] = 1
#             else:
#                 if chess[i][j] != 'W':
#                     check_chess[i][j] = 1
#
# #print(check_chess)
# # 8*8 범위 내에 찾기
# min_sum = N * M
#
# for i in range(N - 7):
#     for j in range(M - 7):
#         chess_sum = 0
#         for a in range(i, i + 8):
#             for b in range(j, j + 8):
#                 chess_sum += check_chess[a][b]
#
#         print("Cs:", chess_sum)
#         if min_sum > chess_sum:
#             min_sum = chess_sum
#
# print(min_sum)
