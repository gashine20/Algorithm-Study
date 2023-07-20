def solution(cards1, cards2, goal):
    answer = "Yes"
    idx1 = -1
    idx2 = -1

    for i in goal:  # "i", "want", "to", "drink", "water"
        if i in cards1:
            if cards1.index(i) == idx1 + 1:  # 순차적으로
                idx1 = cards1.index(i)
            else:
                answer = "No"
                break

        elif i in cards2:
            if cards2.index(i) == idx2 + 1:
                idx2 = cards2.index(i)
            else:
                answer = "No"
                break

    return answer