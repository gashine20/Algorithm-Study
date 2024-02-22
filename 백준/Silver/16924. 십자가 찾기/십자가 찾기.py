import copy

n, m = map(int, input().split())

inputList = [] * n
for _ in range(n):
    inputList.append(list(input().strip()))

finalList = copy.deepcopy(inputList)
count = 0
result = []

for i in range(1, n):
    for j in range(1, m):
        size = 0
        if inputList[i][j] == '*':
            # 현재 위치 저장
            up = down = i
            left = right = j

            while True:
                # 상하좌우
                up = up - 1
                down = down + 1
                left = left - 1
                right = right + 1

                if up >= 0 and down < n and left >= 0 and right < m and inputList[up][j] == '*' and inputList[down][
                    j] == '*' and inputList[i][left] == '*' and inputList[i][right] == '*':
                    finalList[up][j] = finalList[down][j] = finalList[i][left] = finalList[i][right] = finalList[i][
                        j] = '.'
                    size += 1
                else:  # 십자가 x
                    if size > 0:
                        result.append((i + 1, j + 1, size))
                    break

check = True
# print(finalList)
for i in finalList:
    if '*' in i:
        print(-1)
        check = False
        break
if check:
    print(len(result))
    for a, b, c in result:
        print(a, b, c)
