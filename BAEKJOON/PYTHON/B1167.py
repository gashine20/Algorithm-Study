# 트리의 지름

from collections import deque
import sys

input = sys.stdin.readline
V = int(input())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for _ in range(V):
    inputList = list(map(int, input().split(' ')))
    s = inputList[0]

    for i in range(1, len(inputList) - 2, 2):
        graph[s].append((inputList[i], inputList[i + 1]))


def bfs(start, distance):
    myque = deque()

    visited[start] = True
    myque.append((start, distance))

    res = [0, 0]

    while myque:
        now, ndistance = myque.popleft()
        if res[1] < ndistance:
            res[1] = ndistance
            res[0] = now

        for next, dis in graph[now]:
            if not visited[next]:
                visited[next] = True
                myque.append((next, ndistance + dis))

    return res


far_edge, _ = bfs(2, 0)
visited = [False] * (V + 1)
_, answer = bfs(far_edge, 0)

print(answer)
