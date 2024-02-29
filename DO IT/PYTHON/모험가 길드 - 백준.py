import sys
from collections import deque

sys.setrecursionlimit(1000)
input = sys.stdin.readline

# 모험가 길드 개수, 처리 해야 할 쿼리 개수
N, Q = map(int, input().split())

guild = [0] + (list(map(int, input().split())))

alliance = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


# a와 b 동맹 관계 아니면 -1 return 로직 필요
def bfs(a, b):
    myqueue = deque()
    myqueue.append(a)
    count = 0
    result = -1
    while myqueue:
        now = myqueue.popleft()
        count += guild[now]
        visited[now] = True

        # print("now:", now, "count:", count)
        if now == b:
            result = count
            break

        for i in alliance[now]:
            if visited[i]:
                continue

            myqueue.append(i)

    return result


for _ in range(Q):
    option, a, b = map(int, input().split())

    if option == 1:  # 가입
        guild[a] += b
    elif option == 2:  # 탈퇴
        guild[a] = guild[a] - b
    elif option == 3:  # 동맹
        alliance[a].append(b)
        alliance[b].append(a)
    elif option == 4:  # 축하파티
        print(bfs(a, b))
        visited = [False] * (N + 1)  # 초기화
