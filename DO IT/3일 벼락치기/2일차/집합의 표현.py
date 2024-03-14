import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

A = [[] for i in range(n + 1)]
visited = [False] * (n + 1)


def bfs(a, b):
    if a == b:
        return True

    myqueue = deque()
    myqueue.append(a)
    visited[a] = True

    while myqueue:
        now = myqueue.popleft()
        for next in A[now]:
            if next == b:
                return True

            if not visited[next]:
                myqueue.append(next)
                visited[next] = True

    return False


for _ in range(m):
    menu, a, b = map(int, input().split())

    if menu == 0:
        A[a].append(b)
        A[b].append(a)
        print(A)
    elif menu == 1:
        if bfs(a, b):
            visited = [False] * (n + 1)
            print("YES")
        else:
            print("NO")
