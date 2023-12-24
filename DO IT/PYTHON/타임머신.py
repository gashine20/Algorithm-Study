# 벨만 포드 알고리즘

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# direction = [[] for _ in range(N + 1)]
distance = [sys.maxsize] * (N + 1)
# myque = deque()
edges = []


for _ in range(M):
    start, end, time = map(int, input().split())
    edges.append([start, end, time])


distance[1] = 0

for _ in range(N-1):

    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[start] + time < distance[end]:
            distance[end] = distance[start] + time

myCycle = False

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[start] + time < distance[end]:
        myCycle = True

if myCycle:
    print(-1)
else:
    for dis in distance[2:]:
        if dis == sys.maxsize:
            print(-1)
        else:
            print(dis)


# 입력
# for _ in range(M):
#     start, end, time = map(int, input().split())
#
#     found = False
#
#     for info in direction[start]:
#         if info[0] == end:
#             if info[1] > time:  # 더 짧은 시간이 있으면 그걸로
#                 found = True
#                 info[1] = time
#                 break
#
#     if not found:
#         direction[start].append([end, time])

# print(direction)

# 내풀이 - 틀림..
# for _ in range(N-1):
#     # 초기 설정
#     myque.append(1)
#
#     visited = [False for _ in range(N + 1)]
#
#     while myque:
#         now = myque.popleft()
#
#         if visited[now]:
#             continue
#
#         visited[now] = True
#
#         for info in direction[now]:
#             next = info[0]
#             time = info[1]
#
#             if distance[now] + time < distance[next]:
#                 distance[next] = distance[now] + time
#                 myque.append(next)
#
#             # print(distance)

# def contain_negative(distance):
#     for dis in distance[2:]:
#         if dis < 0:
#             return True
#
#     return False
#
#
# if contain_negative(distance):
#     print(-1)
# else:
#     for dis in distance[2:]:
#         if dis == sys.maxsize:
#             print(-1)
#         else:
#             print(dis)

