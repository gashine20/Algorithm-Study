def solution(a, b, n):
    answer = 0
    # 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때,
    # 빈 병 n개를 가져다주면 몇 병을 받을 수 있는지 계산

    while n >= a:
        get_bottle = int((n / a)) * b  # 돌려받음

        n = int(n % a) + get_bottle

        answer += get_bottle

    return answer