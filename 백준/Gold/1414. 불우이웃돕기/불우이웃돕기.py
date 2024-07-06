# 불우이웃돕기
import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
# lanes = [[0 for _ in range(N)] for _ in range(N)]

total = 0
pq = PriorityQueue()
parent = [i for i in range(N)]

# 랜선 데이터 정리
for i in range(N):
    A = input()
    for j in range(N):
        if A[j] != '0':
            temp = 0
            if A[j].isupper():
                temp = ord(A[j]) - 38
            else:
                temp = ord(A[j]) - 96

            total += temp
            if i != j:
                pq.put((temp, i, j))


def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


useEdge = 0
useLanes = 0

# -1인 경우 고려
while useEdge < N - 1 and pq.qsize() > 0:
    w, s, e = pq.get()

    if find(s) != find(e):
        union(s, e)
        useEdge += 1
        useLanes += w


if useEdge == N - 1:
    print(total - useLanes)
else:
    print(-1)
