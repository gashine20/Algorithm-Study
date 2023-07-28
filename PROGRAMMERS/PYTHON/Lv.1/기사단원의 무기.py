def solution(number, limit, power):
    answer = 1
    # 기사단원의 수를 나타내는 정수 number
    for i in range(2, number + 1):
        div = divisor(i)  # 약수 개수
        # print(i, div)
        if div > limit:
            answer += power
        else:
            answer += div

    return answer


def divisor(a):  # 약수의 개수 구함 - 최적화!
    count = 1
    for i in range(2, int(a ** (1 / 2))):  # 루트보다 작게
        if a % i == 0:
            count += 1
    count *= 2

    if int(a ** (1 / 2)) ** 2 == a:
        count += 1

    return count
