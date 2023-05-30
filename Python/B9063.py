# 대지

N = int(input())
area = 0

if N == 1:
    print(area)
else:
    point = [[0 for _ in range(N)] for _ in range(2)]

    # point[0] 은 x 좌표들, point[1]은 y 좌표들
    for i in range(N):
        point[0][i], point[1][i] = map(int, input().split())

    # x(큰값 - 작은값) * y(큰값 - 작은값)
    point[0].sort()
    point[1].sort()

    # print(point)

    x = point[0][N - 1] - point[0][0]
    y = point[1][N - 1] - point[1][0]

    print(x * y)
