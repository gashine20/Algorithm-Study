def solution(park, routes):
    answer = []
    # N(-1,0), W(0,-1), E(0,1), S(1,0)
    op = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}
    x = 0
    y = 0
    h = len(park)
    w = len(park[0])

    # 시작 지점 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x = i
                y = j

    # 이동
    for route in routes:
        d, n = route.split(" ")
        dx = x
        dy = y
        for i in range(int(n)):
            nx = x + op[d][0]
            ny = y + op[d][1]

            if 0 <= nx <= h - 1 and 0 <= ny <= w - 1 and (park[nx][ny] != "X"):
                x, y = nx, ny

            else:
                x, y = dx, dy
                break

        answer = [x, y]

    return answer