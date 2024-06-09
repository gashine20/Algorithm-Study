# K번째 최단경로 찾기
import sys
from queue import PriorityQueue

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [[sys.maxsize for _ in range(k)] for _ in range(n + 1)]
myqueue = PriorityQueue()

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance[start][0] = 0
    myqueue.put((0, start))

    while myqueue.qsize() > 0:
        now = myqueue.get()
        now_node = now[1]
        now_cost = now[0]

        for next, weight in graph[now_node]:
            total_distance = now_cost + weight
            if distance[next][k - 1] > total_distance:  # 계속 갱신이 된다. (6,7)일 때 6이 들어오면 (6,6)으로
                distance[next][k - 1] = total_distance
                myqueue.put((total_distance, next))
                distance[next].sort()  # 정렬
            # print(distance)


dijkstra(1)

for i in range(1, n + 1):
    if distance[i][k - 1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k - 1])
