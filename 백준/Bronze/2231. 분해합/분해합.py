# 분해합
import sys

input = sys.stdin.readline

M = int(input())

generator = 0

for i in range(1, M + 1):
    number = i
    sum_number = 0
    while number != 0:
        sum_number += number % 10
        number //= 10

    if sum_number + i == M:
        generator = i
        break

print(generator)
