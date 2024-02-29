import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

domino = [] * n
for _ in range(n):
    domino.append(list(map(int, input().split(' '))))

queue = deque()
visited = [False] * n


def countRight(idx):
    count = 0
    x = domino[idx][0]
    h = domino[idx][1]
    max_length = x + h

    for a in range(idx + 1, n):
        if domino[a][0] <= max_length:
            max_length = max(max_length, domino[a][0] + domino[a][1])
            #print("1. max_length:", max_length)
            count += 1
        else:
            break

    return count


def countLeft(idx):
    count = 0
    x = domino[idx][0]

    for a in range(idx + 1, n):
        x2 = domino[a][0]
        h2 = domino[a][1]
        if x2 - h2 <= x:
            #print("2. x2:", x2, "-", "h2:", h2, "<=", x)
            x = x2
            count += 1
        else:
            break

    return count


def bfs(idx):
    queue.append(idx)
    visited[idx] = True
    last_idx = idx

    flag = False  # False면 오른쪽으로, True면 왼쪽으로
    # 오른쪽으로 넘어뜨림
    #print("받은 idx:", idx)
    # print("countRight:", countRight(idx))
    # print("countLeft:", countLeft(idx))
    if countRight(idx) < countLeft(idx):
        flag = True

    while queue:
        i = queue.popleft()
        last_idx = i

        #print("i:", i)
        x = domino[i][0]
        h = domino[i][1]

        if flag:  # left
            for a in range(i + 1, n):
                x2 = domino[a][0]
                h2 = domino[a][1]
                if x2 - h2 <= x:
                    x = x2
                    last_idx = a
        else:  # right
            for a in range(i + 1, n):
                if domino[a][0] <= x + h:
                    if not visited[a]:
                        visited[a] = True
                        queue.append(a)

    return last_idx


start = -1
count = 0

while True:
    start = bfs(start + 1)
    count += 1
    #print(start, count)
    if start == n - 1:
        break

print(count)
