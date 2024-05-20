# 집합의 표현
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
A = [i for i in range(n + 1)]


# def findParent(num):
#     if A[num] == num:
#         return num
#     else:
#         return findParent(A[num])

def findParent(num):
    if A[num] != num:
        A[num] = findParent(A[num])
    return A[num]



for i in range(m):
    kind, a, b = map(int, input().split())
    parent1 = findParent(a)
    parent2 = findParent(b)

    if kind == 0:  # a, b 합친다
        if parent1 != parent2:
            A[parent2] = parent1
    elif kind == 1:
        if parent1 == parent2:
            print("YES")
        else:
            print("NO")
