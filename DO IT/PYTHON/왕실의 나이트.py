position = input()

y = ord(position[0]) - ord('a') + 1
x = int(position[1])

# 수평 +2, 수직 +1
# 수직 +2, 수평 +1
# 상, 하, 좌, 우
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

result = 0
for i in range(len(dx)):
    if 1 <= x + dx[i] <= 8 and 1 <= y + dy[i] <= 8:
        result += 1

print(result)