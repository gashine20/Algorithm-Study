import sys

input = sys.stdin.readline

N, M = map(int, input().split())

myMap = [] * N

for _ in range(N):
    myMap.append(list(map(int, input().split())))

print(myMap)