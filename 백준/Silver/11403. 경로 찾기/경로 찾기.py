# 경로 찾기
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

A = [[] for _ in range(N)]
graph = [[] for _ in range(N)]
answer = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))

# graph 생성 & answer 설정
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            graph[i].append(j)
            answer[i][j] = 1

# answer 설정
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if A[i][k] == 1 and A[k][j] == 1:
#                 answer[i][j] = 1

myque = deque()

for i in range(N):
    myque.append(i)
    visited = [False] * N

    while myque:
        now = myque.popleft()
        for next in graph[now]:
            if not visited[next]:
                answer[i][next] = 1
                visited[next] = True
                myque.append(next)

# graph 출력
for ans in answer:
    print(' '.join(str(x) for x in ans))
