import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline

V = int(input())

direction = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
distance = [0] * (V + 1)

for _ in range(V):
    information = list(map(int, input().split()))
    start = information[0]
    for i in range(1, len(information) - 1, 2):
        end = information[i]
        d = information[i + 1]
        direction[start].append((end, d))

answer = 0


def BFS(number):
    queue = deque()

    queue.append(number)
    visited[number] = True

    while queue:
        now = queue.popleft()

        for next, d in direction[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                distance[next] = distance[now] + d
                # print("now =", now, "next =", next, "distance[next] =", distance[next])


BFS(1)  # distance 초기화
Max = 1

for i in range(2, V + 1):
    if distance[Max] < distance[i]:
        Max = i  # 거리 리스트값 중 Max값으로 시작점 재설정

distance = [0] * (V + 1)
visited = [False] * (V + 1)
BFS(Max)
distance.sort()

print(distance[V])
