import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

count = 0

for k in range(N):
    i = 0
    j = N - 1
    while i < j:
        if numbers[i] + numbers[j] == numbers[k]:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif numbers[i] + numbers[j] > numbers[k]:
            j -= 1
        else:
            i += 1

print(count)
