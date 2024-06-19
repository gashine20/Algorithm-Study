# 게임 개발
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
D = [0] * (N + 1)
building = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)
buildTime = [0] * (N + 1)

for i in range(1, N + 1):
    information = list(map(int, input().split()))
    buildTime[i] = information[0]

    for info in information[1:-1]:
        building[info].append(i)
        D[i] += 1

myque = deque()

for i in range(1, N + 1):
    if D[i] == 0:
        answer[i] = buildTime[i]
        myque.append(i)

while myque:
    now = myque.popleft()

    for next in building[now]:
        D[next] -= 1
        answer[next] = max(answer[next], answer[now] + buildTime[next])  # answer 수정
        if D[next] == 0:
            # myque에 넣고
            myque.append(next)

    # print(answer)

for ans in answer[1:]:
    print(ans)
