# 가로수
# 여러 수 최대공약수
import sys

input = sys.stdin.readline
from math import gcd

n = int(input())
position = [] * n
distance = [] * (n - 1)

for i in range(n):
    position.append(int(input()))

for i in range(1, n):
    distance.append(position[i] - position[i - 1])

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
