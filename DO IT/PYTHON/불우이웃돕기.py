import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
pq = PriorityQueue()
ran_sum = 0

for i in range(N):
    tempc = list(input())
    for j in range(N):
        temp = 0
        if 'a' <= tempc[j] <= 'z':
            temp = ord(tempc[j]) - ord('a') + 1
        elif 'A' <= tempc[j] <= 'Z':
            temp = ord(tempc[j]) - ord('A') + 27

        ran_sum += temp

        if i != j and temp != 0:
            pq.put((temp, i, j))

parent = [0] * N

for i in range(N):
    parent[i] = i


def find(a):
    if a == parent[a]:
        return a
    else:
        return find(parent[a])


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


count = 0
useEdge = 0

while pq.qsize() > 0:
    w, s, e = pq.get()

    if find(s) != find(e):
        union(s, e)
        useEdge += 1
        count += w
        # print("s:",s,"e",e,useEdge)

if useEdge == N - 1:
    print(ran_sum - count)
else:
    print(-1)
