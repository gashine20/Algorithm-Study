import sys

input = sys.stdin.readline

n = int(input())
plan = list(map(str, input().split()))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x = 1
y = 1

for direction in plan:
    if direction == 'R':
        if y + 1 > n:
            continue
        y += 1
    elif direction == 'L':
        if y - 1 < 1:
            continue
        y -= 1
    elif direction == 'U':
        if x - 1 < 1:
            continue
        x -= 1
    elif direction == 'D':
        if x + 1 > n:
            continue
        x += 1

print(x, y)
