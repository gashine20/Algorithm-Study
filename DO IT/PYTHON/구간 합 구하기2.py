import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 2차원 배열의 크기, 구간 합 질의의 개수

num = [[0] * (N + 1)]
S = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(N):
    num.append([0] + list(map(int, input().split())))

S[1][1] = num[0][0]

# # 1행 1열 설정
# for i in range(1, N):
#     S[0][i] = S[0][i - 1] + num[0][i]
#
# for j in range(1, N):
#     S[j][0] = S[j - 1][0] + num[j][0]

# 합 배열 구하기
for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + num[i][j]

# for i in range(N):
#     for j in range(N):
#         print(S[i][j], end=' ')
#
#     print()

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # print(x2-1, "," , y2-1, "/",  x2-1, ",", y1-2, "/",  x1-2, ",", y2-1, "/",  x1-2, ",", y1-2)
    result = S[x2][y2] - S[x2][y1 - 1] - S[x1 - 1][y2] + S[x1 - 1][y1 - 1]
    print(result)
