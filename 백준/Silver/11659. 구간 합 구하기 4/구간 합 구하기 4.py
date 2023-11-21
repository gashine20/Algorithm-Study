# 수 N개가 주어졌을 때 i번째 수에서 j번째 수까지 합을 구하라
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

# 1. 합 배열 만들기
temp = 0
prefix_sum = [0]
for num in numbers:
    temp += num
    prefix_sum.append(temp)

# 2. 합 배열에서 구간 합 구하기
for _ in range(M):
    i, j = map(int, input().split())

    print(prefix_sum[j]-prefix_sum[i-1])