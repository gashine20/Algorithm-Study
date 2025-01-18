# 연사자 끼워넣기

from itertools import permutations
import sys

N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
op = []

for i in range(len(operator)):
    for j in range(operator[i]):
        op.append(i)

max_result = -1 * sys.maxsize
min_result = sys.maxsize


def calculate(a, b, index):
    if index == 0:
        return a + b
    elif index == 1:
        return a - b
    elif index == 2:
        return a * b
    elif index == 3:
        if a < 0 < b:
            a = -1 * a
            return -1 * (a // b)
        return a // b


for indexes in permutations(op, N-1):
    result = num[0]
    for i in range(1, len(num)):
        result = calculate(result, num[i], indexes[i - 1])

    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
