# 버블정렬

n = int(input())

A = []
for _ in range(n):
    A.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]  # swap

for a in A:
    print(a)
