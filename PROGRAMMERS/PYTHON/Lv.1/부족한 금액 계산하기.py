def solution(price, money, count):
    answer = -1
    charge = 0
    increase_price = price

    for i in range(count):
        charge += increase_price
        increase_price += price

    if charge - money < 0:
        answer = 0
    else:
        answer = charge - money

    return answer