def solution(s, skip, index):
    answer = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in skip:
        alpha = alpha.replace(i, "")

    for i in s:  # "aukks"
        next = alpha.index(i) + index
        if next >= len(alpha):
            next %= len(alpha)

        answer += alpha[next]

    return answer