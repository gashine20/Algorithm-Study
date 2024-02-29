import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
queue = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

print(in_degree)
print(graph)

# 진입 차수가 0이면 추가
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

answer = []
while queue:
    now = queue.popleft()
    answer.append(now)

    # print("in_degree:", in_degree)

    for next in graph[now]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            queue.append(next)

for a in answer:
    print(a, end=' ')
