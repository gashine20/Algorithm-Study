# 최소 스패닝 트리
# 모든 노드를 연결할 때 사용된 에지들의 가중치의 합을 최소로 하는 트리
# + 유니온 파인드
import sys
from queue import PriorityQueue

input = sys.stdin.readline

V, E = map(int, input().split())
weight = [[] for _ in range(V)]
parent = [0] * (V + 1)
pq = PriorityQueue()

for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    A, B, C = map(int, input().split())
    pq.put((C, A, B))


def find(a):
    if a == parent[a]:
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
result = 0

while useEdge < V - 1:
    w, s, e = pq.get()

    if find(s) != find(e):
        union(s, e)
        useEdge += 1
        result += w

print(result)
