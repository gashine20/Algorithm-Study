def solution(N, stages):
    answer = []
    percent = {}
    # 전체 스테이지의 개수 N,

    for i in range(1,N+1):
        user = 0
        fail = 0
        for stage in stages: #사용자 도전
            if stage >= i:
                user+=1

            if stage==i:
                fail+=1

        if user == 0 : # 런타임 에러
            percent[i] = 0
        else:
            percent[i] = fail/user

    # print(percent)
    # 이걸 어떻게 외워..
    # 내림차순 정렬 하는 방법.....
    percent = sorted(percent.items(), key = lambda item: item[1], reverse = True)
    # print(percent)

    for per in percent:
        answer.append(per[0])

    return answer