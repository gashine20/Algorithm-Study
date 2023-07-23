def solution(food):
    answer = ''
    # food를 2로 나눔
    # 그 갯수만큼 추가

    for i in range(1, len(food)):
        count = int(food[i] / 2)
        for _ in range(count):
            answer = answer + str(i)

    answer = answer + str(0)

    # 반대로
    for i in range(len(food) - 1, 0, -1):
        count = int(food[i] / 2)
        for _ in range(count):
            answer = answer + str(i)
    return answer