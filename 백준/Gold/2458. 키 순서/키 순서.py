import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

relationOut = [[] for _ in range(n + 1)]
relationIn = [[] for _ in range(n+1)]

visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    relationOut[a].append(b)  # a->b
    relationIn[b].append(a)  # b<-a

def inCount(a):  # 들어오는거
    global visited
    count = 0

    myqueue = deque()
    myqueue.append(a)
    visited[a] = True

    while myqueue:
        now = myqueue.popleft()

        for next in relationIn[now]:
            if not visited[next]:
                count += 1
                visited[next] = True
                myqueue.append(next)

    return count

def outCount(a):
    count = 0
    myqueue = deque()
    myqueue.append(a)
    visited[a] = True

    while myqueue:
        now = myqueue.popleft()

        for next in relationOut[now]:
            if not visited[next]:
                count += 1
                visited[next] = True
                myqueue.append(next)

    return count


answer = 0
for i in range(1, n + 1):
    # 들어오는거
    count1 = inCount(i)
    visited = [False] * (n + 1)
    # 나가는거
    count2 = outCount(i)
    visited = [False] * (n + 1)

    if count1 + count2 >= n - 1:
        answer += 1

print(answer)
