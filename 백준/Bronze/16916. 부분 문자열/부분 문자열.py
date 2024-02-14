import sys

input = sys.stdin.readline

S = input().strip()
P = input().strip()

result = 0

if P in S:
    result = 1

print(result)
