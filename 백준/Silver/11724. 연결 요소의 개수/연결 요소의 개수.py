import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

answer = 0


def dfs(index):  # 깊이탐색 - visited를 처리하는
    visited[index] = True

    for a in A[index]:
        if not visited[a]:
            dfs(a)

        #print(visited)


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
