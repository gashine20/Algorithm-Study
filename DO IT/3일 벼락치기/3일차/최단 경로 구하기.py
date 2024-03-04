import sys
from queue import PriorityQueue

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

distance = [sys.maxsize] * (v + 1)
visited = [False] * (v + 1)
myList = [[] for _ in range(v + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    myList[u].append((v, w))

q = PriorityQueue()

q.put((0, start))  # 값, 시작점
distance[start] = 0

while q.qsize() > 0:
    now = q.get()
    c_v = now[1]

    if visited[c_v]:
        continue
    visited[c_v] = True

    for tmp in myList[c_v]:  # 정점, 거리
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))

# print(distance)
# print(visited)
for i in range(1, v + 2):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
