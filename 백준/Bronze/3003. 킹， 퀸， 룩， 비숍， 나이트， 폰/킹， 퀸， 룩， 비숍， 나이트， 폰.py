# 킹, 퀸, 룩, 비숍, 나이트, 폰
# 1, 1, 2, 2, 2, 8

correct_count = [1, 1, 2, 2, 2, 8]
white_piece = list(map(int, input().split()))

for i in range(len(white_piece)):
    white_piece[i] = correct_count[i] - white_piece[i]

for piece in white_piece:
    print(piece, end=' ')