import sys

input = sys.stdin.readline

A = list(map(str, input().rstrip().split('-')))

minSum = 0
print(A)
# 처음


for i in range(0, len(A)):
    B = A[i].split('+')
    B_sum = 0
    for b in B:
        B_sum += int(b)

    if i == 0:
        minSum += B_sum
    else:
        minSum -= B_sum

print(minSum)
