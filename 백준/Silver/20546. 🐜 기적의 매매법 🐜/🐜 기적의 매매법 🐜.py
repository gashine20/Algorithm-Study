# 기적의 매매법

# 3일째 주가 하락 : 다음날 주 삼
# 3일째 주가 상승 : 다음날 주 팜

jun_money = int(input())
sung_money = jun_money
stock_price = list(map(int, input().split()))

jun_stock_price = 0
sung_stock_price = 0


def check_trend(index):
    if stock_price[index - 1] < stock_price[index - 2] < stock_price[index - 3]:
        return 'down'
    elif stock_price[index - 1] > stock_price[index - 2] > stock_price[index - 3]:
        return 'up'
    return ''


for i in range(len(stock_price) - 1):
    price = stock_price[i]
    if price <= jun_money:
        jun_stock_price = jun_money // price
        jun_money = jun_money % price

    if i >= 3:
        trend = check_trend(i)
        if trend == 'down':  # 3일째 주가 하락 : 주 삼
            if price <= sung_money:
                sung_stock_price += sung_money // price
                sung_money = sung_money % price
        elif trend == 'up':  # 3일째 주가 상승 : 주 팜
            sung_money += sung_stock_price * stock_price[i]
            sung_stock_price = 0

jun_money += jun_stock_price * stock_price[len(stock_price) - 1]
sung_money += sung_stock_price * stock_price[len(stock_price) - 1]

if jun_money > sung_money:
    print('BNP')
elif jun_money < sung_money:
    print('TIMING')
else:
    print('SAMESAME')
