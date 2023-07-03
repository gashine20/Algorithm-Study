# 체스판 다시 칠하기

n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())