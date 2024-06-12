# 오민식의 고민
# 벨만-포드
import sys

input = sys.stdin.readline

N, s, e, M = map(int, input().split())
graph = []

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph.append((start, end, cost))

money = list(map(int, input().split()))

result = [-sys.maxsize] * N
result[s] = money[s] # 출발 초기화

for i in range(N + 101):
    for start, end, cost in graph:
        print("money:", result[start] - cost + money[end])
        if result[start] == -sys.maxsize:  # 출발 노드가 미 방문 노드면 skip
            continue
        elif result[start] == sys.maxsize:
            result[end] = sys.maxsize
        # 더 많은 돈을 벌 수 있는 새로운 경로가 있는 경우 값 업데이트
        elif result[end] < result[start] - cost + money[end]:
            result[end] = result[start] - cost + money[end]
            if i >= N - 1:  # N-1번 돌았을 때도 양수 사이클이면 max로 지정
                result[end] = sys.maxsize

        print(result)

if result[e] == -sys.maxsize:  # 도착 불가능
    print("gg")
elif result[e] == sys.maxsize:  # 양수 사이클 -> 무한대로 돈을 벌 수 있는 경우
    print("Gee")
else:
    print(result[e])
