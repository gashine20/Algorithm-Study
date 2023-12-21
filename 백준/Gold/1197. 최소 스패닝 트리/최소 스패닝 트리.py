import sys
from queue import PriorityQueue

input = sys.stdin.readline
pq = PriorityQueue()

V, E = map(int, input().split())
parent = [0] * (V + 1)

for i in range(V + 1):
    parent[i] = i

for _ in range(E):
    s, e, w = map(int, input().split())
    pq.put((w, s, e))


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])  # 부모가 있는 경우
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


useEdge = 0
result = 0

while useEdge < V - 1:
    w, s, e = pq.get()
    if find(s) != find(e):  # 같은 부모가 아닌 경우만 연결
        union(s, e)
        result += w
        useEdge += 1

print(result)
