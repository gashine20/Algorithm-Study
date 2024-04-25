# 가로수
# 여러 수 최대공약수
import sys

input = sys.stdin.readline
from math import gcd

n = int(input())
a = int(input()) # 처음 위치

distance = [] * (n - 1)

for _ in range(n-1):
    num = int(input())
    distance.append(int(input())-a)
    a = num

# print(distance)

# distance의 최대공약수 구하기
g = distance[0]
for i in range(1, len(distance)):
    g = gcd(g, distance[i])

# print("최대공약수", maxMultiply)

# 최대공약수 거리 만큼 심기 - 하나씩 다 담지 말고 거리....
count = 0
for each in distance:
    count += each // g - 1

print(count)
