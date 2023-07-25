def solution(lottos, win_nums):
    answer = []
    rank = [6, 5, 4, 3, 2]
    m = 0
    lost = lottos.count(0)

    for lotto in lottos:
        if lotto in win_nums:  # 몇 개 맞는지 계산
            m += 1

            # m = 0 : 다 다른 숫자 거나 다 0
    if m + lost == 0:  # lost = 0 : 다 다른 숫자
        worst_rank = 6
        best_rank = 6
    elif m == 0 and lost == 6:  # lost = 6 : 다 0
        worst_rank = 6
        best_rank = 1
    elif m == 6 and lost == 0:  # m = 6 : 다 같은 숫자
        worst_rank = 1
        best_rank = 1
    else:
        if m + lost < 2:
            best_rank = 6
        else:
            best_rank = rank.index(m + lost) + 1
        if m < 2:
            worst_rank = 6
        else:
            worst_rank = rank.index(m) + 1

    answer = [best_rank, worst_rank]

    return answer