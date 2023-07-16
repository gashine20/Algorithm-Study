# 추억 점수
def solution(name, yearning, photo):
    answer = []

    for people in photo:
        score = 0
        for p in people:
            if p in name:
                idx = name.index(p)
                score += yearning[idx]

        answer.append(score)

    return answer