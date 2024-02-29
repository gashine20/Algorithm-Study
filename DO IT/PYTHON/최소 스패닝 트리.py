import sys
from queue import PriorityQueue

input = sys.stdin.readline

V, E = map(int, input().split())
queue = PriorityQueue()  # PriorityQueue로 선언
parent = [0] * (V + 1)

for i in range(V + 1):  # 부모는 자기 자신으로 초기화
    parent[i] = i

for _ in range(E):
    s, e, w = map(int, input().split())
    queue.put((w, s, e))


def find(a):  # 부모 찾기
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):  # 합치기
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


useEdge = 0
result = 0

while useEdge < V - 1:  # 노드 -1 간선만큼
    w, s, e = queue.get()
    print("s:", s, "e:", e, "find(s):", find(s), "find(e):", find(e))
    if find(s) != find(e):
        union(s, e)
        result += w
        print("result:", result)
        useEdge += 1

print("end", result)
