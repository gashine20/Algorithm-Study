import sys

input = sys.stdin.readline

s = list(map(int, input().split()))

result = s[0]

for i in range(1, len(s)):
    if s[i] <= 1 or result <= 1:
        result += s[i]
    else:
        result *= s[i]

print(result)
