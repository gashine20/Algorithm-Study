N = int(input())

num = []

num = map(int, input().split())

v = int(input())

count = 0
for n in num:  # 같은 것이 있으면 count 1씩 증가
    if n == v:
        count += 1

print(count)