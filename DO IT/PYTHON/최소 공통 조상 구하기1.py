# 최소 공통 조상 구하기
# BFS 사용
import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
tree = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

depth = [0] * (N + 1)
parent = [0] * (N + 1)  # 부모 노드 저장

for _ in range(N - 1):
    node1, node2 = map(int, input().split())

    tree[node1].append(node2)
    tree[node2].append(node1)


# print(tree)


def BFS(node):
    myDeque = deque()
    myDeque.append(node)
    visited[node] = True

    level = 1
    now_size = 1
    count = 0

    while myDeque:
        now_node = myDeque.popleft()

        for next_node in tree[now_node]:
            if not visited[next_node]:
                visited[now_node] = True
                myDeque.append(next_node)

                parent[next_node] = now_node
                depth[next_node] = level

        count += 1
        if now_size == count:
            count = 0  # 초기화
            now_size = len(myDeque)
            level += 1


BFS(1)


# print(parent)


def LCA(a, b):
    # 노드 깊이 다르면 부모 노드로 1씩 올리고
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp

    while depth[a] != depth[b]:
        b = parent[b]

    # 노드 깊이 맞추고 난 후
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


# find LCA
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(str(LCA(a, b)) + "\n")

