import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
indegree = [0] * (n + 1)
relation = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)

for i in range(1, n + 1):
    inputList = list(map(int, input().split()))
    cost[i] = inputList[0]
    for pre in inputList[1:len(inputList) - 1]:
        relation[pre].append(i)
        indegree[i] += 1

# print("relation:",relation)
# print("indegree:",indegree)

myqueue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        myqueue.append(i)

result = [0] * (n + 1)
while myqueue:
    now = myqueue.popleft()

    for next in relation[now]:
        indegree[next] -= 1

        result[next] = max(result[next], result[now] + cost[next])
        if indegree[next] == 0:
            myqueue.append(next)

for i in range(1, n + 1):
    print(result[i] + cost[i])
