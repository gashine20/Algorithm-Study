def solution(n, m, section):
    answer = 0
    paint = [0 for _ in range(n)]

    for i in section:
        paint[i - 1] = 1  # index 1,2,5 칠해짐

    for y in range(0, n - m + 1, m):  # m 단위로
        if paint[y:y + m].count(1) > 0:  # 1이 있다면
            paint[y:y + m] = [0 for _ in range(m)]
            answer += 1

    return answer