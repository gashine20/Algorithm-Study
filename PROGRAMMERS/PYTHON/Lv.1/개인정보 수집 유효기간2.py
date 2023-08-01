def calculateDay(day):
    y, m, d = map(int, day.split("."))
    return y * 12 * 28 + m * 28 + d


def solution(today, terms, privacies):
    answer = []
    term = {}

    today_cal = calculateDay(today)

    # term dict으로 변환
    for t in terms:
        a, b = t.split(" ")
        b = int(b)
        term[a] = b

    index = 1

    # 계산
    for privacy in privacies:
        start, term_type = privacy.split(" ")
        start_cal = calculateDay(start)

        privacy_term = term[term_type]
        if today_cal >= start_cal + privacy_term * 28:
            answer.append(index)

        index += 1

    return answer