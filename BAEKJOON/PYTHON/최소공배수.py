#    100 120
# 2 | 50 60
# 2 | 25 30
# 5 | 5  6
# 더이상 나눔 x
import math

a, b = map(int, input().split())
minMultiple = 1

# 100 120 최대 공약수 : 20
# 최대 공약수를 먼저 구하고 나눈걸 곱하기
# 최소공배수 = 최대공약수 * 나머지들

# 최대 공약수 구하기

# a 작은수
if b < a:
    a, b = b, a

# if int(math.sqrt(a)) > 1:
#     for i in range(2, int(math.sqrt(a)) + 1):
#         if a % i == 0 and b % i == 0:
#             minMultiple = i

for i in range(2, a+1):
    if a % i == 0 and b % i == 0:
        minMultiple = i

print(minMultiple * int(a / minMultiple) * int(b / minMultiple))
