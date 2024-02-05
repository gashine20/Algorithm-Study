import sys

input = sys.stdin.readline

N = int(input())

adventurer = list(map(int, input().split()))

adventurer.sort()
print(adventurer)

group = 0
count = 0  # 현재 그룹의 사람 수

for data in adventurer:
    # 넣고
    count += 1
    if count >= data:  # 넣은 count 수가 data보다 크거나 같으면
        group += 1
        count = 0  # 초기화

print(group)
