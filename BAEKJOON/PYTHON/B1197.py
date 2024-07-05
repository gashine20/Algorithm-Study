# 최소 스패닝 트리
# 모든 노드를 연결할 때 사용된 에지들의 가중치의 합을 최소로 하는 트리
# + 유니온 파인드
import sys
from queue import PriorityQueue

input = sys.stdin.readline

V, E = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (V + 1)

for _ in range(E):
    A, B, C = map(int, input().split())
    pq.put((C, A, B))

for i in range(1, V + 1):
    parent[i] = i

useEdge = 0
answer = 0


def find(a):  # 부모 찾아주는 함수
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):  # 각각 부모를 찾아서 그 부모의 참조를 변경
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


while useEdge < V - 1:
    w, s, e = pq.get()

    if find(s) != find(e):
        union(s, e)
        answer += w
        useEdge += 1

print(answer)
