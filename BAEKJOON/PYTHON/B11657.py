# 타임머신
# 벨만-포드 음수 가중치가 있는 경우
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
result = [sys.maxsize] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

result[1] = 0

for _ in range(N - 1):

    for start, end, time in graph:  # result[start]!=sys.maxsize 조건이 있어야 1에서 출발할 수 있는 노선이 있는지 확인 가능하다.
        if result[start] != sys.maxsize and result[end] > result[start] + time:
            result[end] = result[start] + time

# 음수 사이클 존재 여부 확인
# 에지 개수만큼 반복

mCycle = False
for start, end, time in graph:
    if result[start] != sys.maxsize and result[end] > result[start] + time:
        mCycle = True

if not mCycle:
    for i in range(2, N + 1):
        if result[i] != sys.maxsize:
            print(result[i])
        else:
            print(-1)
else:
    print(-1)
