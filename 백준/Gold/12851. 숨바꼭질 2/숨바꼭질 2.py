# 숨바꼭질2

import sys
from collections import deque

input = sys.stdin.readline()

N, K = map(int, input.split())

MAX_SIZE = 100000
move_count = [0] * (MAX_SIZE + 1)  # 특정 시간에 도달한 경우의 수
visited = [-1] * (MAX_SIZE + 1)


def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        current, cnt = queue.popleft()

        if current == K:
            move_count[cnt] += 1
        else:
            for next in (current - 1, current + 1, 2 * current):
                if 0 <= next <= MAX_SIZE:
                    # 처음 방문하거나, 동일 시간에 방문 가능하면
                    if visited[next] == -1 or visited[next] == cnt + 1:
                        visited[next] = cnt + 1
                        queue.append((next, cnt + 1))


bfs(N)

for time, count in enumerate(move_count):
    if count > 0:
        print(time)
        print(count)
        break
