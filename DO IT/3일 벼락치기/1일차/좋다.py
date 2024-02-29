import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

A.sort()

answer = 0

for k in range(n):
    i = 0
    j = n - 1
    while i < j:
        A_sum = A[i] + A[j]
        if A_sum < A[k]:
            i += 1
        elif A_sum > A[k]:
            j -= 1
        else:  # 같으면
            if i != k and j != k:
                answer += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1

print(answer)
