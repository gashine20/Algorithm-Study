# 숨바꼭질
import sys
from collections import deque

MIN_SIZE = 0
MAX_SIZE = 100000

N, K = map(int, input().split())
visited = [-1] * (MAX_SIZE + 1)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        now = queue.popleft()
        # print(now, "->", end = "")
        if now == K:
            # print(":", visited[K])
            print(visited[K])
            break
        else:
            for next in (now - 1, now + 1, 2 * now):
                if 0 <= next <= MAX_SIZE:
                    if visited[next] == -1:
                        visited[next] = visited[now] + 1
                        queue.append(next)


bfs(N)
