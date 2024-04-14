# 최대공약수 구하는 함수
def gcd(x, y):
    while x % y != 0:
        mod = x % y
        x = y
        y = mod
    return y


a, b = map(int, input().split())
c, d = map(int, input().split())

g1 = gcd(b, d)  # 최대 공약수
demon = b * d // g1

mole = a * (d // g1) + c * (b // g1)
g2 = gcd(demon, mole)
print(mole // g2, demon // g2)
