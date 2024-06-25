# 줄 세우기
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

students = [[] for _ in range(N + 1)]
D = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    students[A].append(B)
    D[B] += 1

myque = deque()

for i in range(1, N + 1):
    if D[i] == 0:
        myque.append(i)

while myque:
    now = myque.pop()
    print(now, end=" ")

    for next in students[now]:
        D[next] -= 1

        if D[next] == 0:
            myque.append(next)
