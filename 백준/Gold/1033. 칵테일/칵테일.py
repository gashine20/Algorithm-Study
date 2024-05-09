# 칵테일
# 1. DFS 사용
# 2. 첫 시작 노드의 최소공배수 구하기
# 3. 인접노드 * (비율)
# 4. 업데이트 된 리스트 최대 공약수로 약분

N = int(input())
graph = [[] for _ in range(N)]
visited = [False] * N
ingredient = [0] * N
lcm = 1


def gcd(a, b):  # 최대 공약수
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))
    lcm = lcm * p * q // gcd(p, q)  # 최소공배수

def dfs(start):  # 시작 노드, 최소공배수
    visited[start] = True

    for next in graph[start]:
        if not visited[next[0]]:
            ingredient[next[0]] = ingredient[start] * next[2] // next[1]
            dfs(next[0])


ingredient[0] = lcm
dfs(0)

greatest = ingredient[0]
for ingred in ingredient:  # 최대공약수 구하기
    greatest = gcd(greatest, ingred)

for i in range(N): # 최대공약수로 약분
    ingredient[i] = int(ingredient[i] // greatest)

for ingred in ingredient:
    print(ingred, end=" ")
