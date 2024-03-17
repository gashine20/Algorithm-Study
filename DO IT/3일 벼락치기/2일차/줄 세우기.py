import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

relation = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())

    relation[a].append(b)
    indegree[b] += 1

myqueue = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        myqueue.append(i)

while myqueue:
    now = myqueue.popleft()
    print(now, end=" ")

    for next in relation[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            myqueue.append(next)
