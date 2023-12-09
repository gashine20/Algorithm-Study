# 위상 정렬
from collections import deque

N = int(input())

building = [[] for _ in range(N + 1)]
cost = [0] * (N + 1)
indegree = [0] * (N + 1)

for i in range(1, N + 1):
    inputList = list(map(int, input().split(' ')))[:-1]
    cost[i] = inputList[0]

    for j in range(1, len(inputList)):
        building[inputList[j]].append(i)
        indegree[i] += 1

# print(building)
# print(cost)
# print(indegree)

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:  # 제약이 없으면
        queue.append(i)

result = [0] * (N + 1)

while queue:
    now = queue.popleft()

    for next in building[now]:
        indegree[next] -= 1
        # 시간 업데이트
        result[next] = max(result[next], result[now] + cost[now])
        if indegree[next] == 0:
            queue.append(next)

# print("result", result)
for i in range(1, N + 1):
    print(result[i] + cost[i])
