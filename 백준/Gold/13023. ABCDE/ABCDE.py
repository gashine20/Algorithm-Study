import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

friend = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())

    friend[a].append(b)
    friend[b].append(a)

answer = 0


def DFS(number, depth):
    if depth == 5:
        return True

    visited[number] = True

    # print("visited", number, " ,count", depth)
    for i in friend[number]:
        if not visited[i]:
            if DFS(i, depth + 1):
                return True
    visited[number] = False  # 초기화


for i in range(N):
    if DFS(i, 1):
        answer = 1
        break
    # print("-------------")

print(answer)
