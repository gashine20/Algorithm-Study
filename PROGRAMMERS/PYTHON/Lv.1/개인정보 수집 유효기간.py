def solution(today, terms, privacies):
    answer = []
    term = {}

    today_year, today_month, today_day = map(int, today.split("."))

    # term dict으로 변환
    for t in terms:
        a, b = t.split(" ")
        b = int(b)
        term[a] = b

    index = 1
    for privacy in privacies:
        start, term_type = privacy.split(" ")
        start_year, start_month, start_day = map(int, start.split("."))
        privacy_term = term[term_type]

        # 12월 넘으면 1년 높이고 월은 12빼고
        if start_month + privacy_term > 12:
            start_year += 1
            start_month = start_month + privacy_term - 12
        else:
            start_month += privacy_term

        # start_day가 1일이면 월은 1빼고 일 = 28
        # 이때 월 1 뺐을 때 1월달이였으면 12월달, 1년 빼고
        if start_day == 1:
            if start_month == 1:
                start_year -= 1
                start_month = 12
            else:
                start_month -= 1
            start_day = 28
        else:
            start_day -= 1
        print(start_year, start_month, start_day)

        # 지난거
        if today_year > start_year:
            answer.append(index)
        elif today_year >= start_year:
            if today_month > start_month:
                answer.append(index)
            elif today_month >= start_month:
                if today_day > start_day:
                    answer.append(index)

        index += 1

    return answer