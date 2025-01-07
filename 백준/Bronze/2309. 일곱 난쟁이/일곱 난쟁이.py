# 일곱 난쟁이
import sys

input = sys.stdin.readline
height = []
for _ in range(9):
    height.append(int(input()))

height.sort()
total_sum = sum(height)
want_height = total_sum - 100


def printHeight(i, j):
    for k in range(len(height)):
        if k != i and k != j:
            print(height[k])


check = False
for i in range(8):
    for j in range(i + 1, 9):
        height_sum = height[i] + height[j]
        if height_sum == want_height:
            printHeight(i, j)
            check = True
    if check:
        break
