# 숫자 정사각형

N, M = map(int, input().split())

square = []
for _ in range(N):
    line = input()
    square.append([int(char) for char in line])

max_distance = min(N, M)
result = 1

for distance in range(1, max_distance):
    for i in range(N - distance):
        flag = False
        for j in range(M - distance):
            if square[i][j] == square[i + distance][j] == square[i][j + distance] == square[i + distance][j + distance]:
                result = (distance + 1) * (distance + 1)
                flag = True
                break
        if flag:
            break

print(result)
