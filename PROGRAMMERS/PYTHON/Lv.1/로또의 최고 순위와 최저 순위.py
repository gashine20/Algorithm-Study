def solution(lottos, win_nums):
    answer = []
    m = 0
    lost = lottos.count(0)

    for lotto in lottos:
        if lotto in win_nums:  # 몇 개 맞는지 계산
            m += 1

    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    best_rank = rank.get(m+lost)
    worst_rank = rank.get(m)

    answer = [best_rank, worst_rank]

    return answer
