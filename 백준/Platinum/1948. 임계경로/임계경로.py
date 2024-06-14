# 임계경로

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
reverseGraph = [[] for _ in range(n + 1)]
D = [0] * (n + 1)
time = [0] * (n + 1)

for _ in range(m):
    s, e, t = map(int, input().split())

    graph[s].append((e, t))
    reverseGraph[e].append((s, t))
    D[e] += 1

start, end = map(int, input().split())

queue = deque()

queue.append(start)

while queue:
    now = queue.popleft()

    for next, t in graph[now]:
        D[next] -= 1
        time[next] = max(time[next], time[now] + t)

        if D[next] == 0:
            queue.append(next)

# end까지 가는데에 걸리는 최대 시간
print(time[end])
# print(time)

# 에지 뒤집기
myque = deque()
resultCount = 0
visited = [False] * (n + 1)

myque.append(end)
visited[end] = True

while myque:
    now = myque.popleft()

    for next, t in reverseGraph[now]:
        if time[next] + t == time[now]:  # 1분도 쉬지 않는 도로 체크
            resultCount += 1
            if not visited[next]:
                myque.append(next)
                visited[next] = True

print(resultCount)
