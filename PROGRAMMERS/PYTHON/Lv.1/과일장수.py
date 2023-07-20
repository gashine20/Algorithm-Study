def solution(k, m, score):
    answer = 0

    # 1점부터 k점까지의 점수로 분류
    # 한 상자에 사과를 m개씩 담아 포장

    score.sort(reverse=True)
    for i in range(int(len(score) / m)):  # 나올 수 있는 박스 수
        little_score = score[(i + 1) * m - 1]
        # print(little_score)
        answer += little_score * m

    return answer