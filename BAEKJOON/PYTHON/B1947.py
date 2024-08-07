# 선물 전달
import sys

input = sys.stdin.readline
N = int(input())

D = [0] * (N + 1)
D[2] = 1

mod = 1000000000

for i in range(3, N + 1):
    D[i] = (i - 1) * (D[i - 2] + D[i - 1]) % mod


print(D[N])
