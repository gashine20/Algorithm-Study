def solution(s):
    answer = []

    alph = {}
    # 처음이냐 아니냐
    for i in range(len(s)):
        if s[i] in alph:  # 앞에 있으면
            answer.append(i - alph[s[i]])  # 몇 칸 차이인지
            alph[s[i]] = i  # 다시 갱신
            pass
        else:  # 처음이면
            answer.append(-1)
            alph[s[i]] = i

    return answer
