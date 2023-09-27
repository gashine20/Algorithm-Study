X = int(input())  # 영수증에 적힌 금액
N = int(input())  # 구매한 물건 종류 수

price = 0
for i in range(N):
    a, b = list(map(int, input().split()))
    price += a * b

if price == X:
    print("Yes")
else:
    print("No")