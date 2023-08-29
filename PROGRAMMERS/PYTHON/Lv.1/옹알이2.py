def solution(babbling):
    answer = 0

    announce = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for ann in announce:
            if ann * 2 not in bab:  # ann이 연속적이지 않으면
                bab = bab.replace(ann, ' ')  # 그부분을 하나의 띄어쓰기로
                # 예)  'yayae'에서 'aya'는 발음 가능하므로 ''으로 대체하면 'ye'가 남는다. 'ye' 또한 ''으로 대체하면 최종적으로는 ''이 남게 된다.

        if bab.isspace():
            answer += 1

    return answer