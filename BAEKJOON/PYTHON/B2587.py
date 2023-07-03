# 대표값2

a = []
for _ in range(5):
    b = int(input())
    a.append(b)

a.sort()

sum = 0
for i in a:
    sum += i

print(int(sum / 5))
print(a[2])
