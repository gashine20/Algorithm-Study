import sys

input = sys.stdin.readline
n, m = map(int, input().split())

A = list(map(int, input().split()))

A_sum = [0] * (n + 1)
for i in range(1, n + 1):
    A_sum[i] = A_sum[i - 1] + A[i - 1]

for _ in range(m):
    start, end = map(int, input().split())
    print(A_sum[end] - A_sum[start - 1])
