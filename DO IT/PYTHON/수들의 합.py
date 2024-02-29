s = int(input())

sum = 0
i = 1
ans = 0

while s >= sum:
    sum += i
    i += 1
    ans += 1

print(ans - 1)
