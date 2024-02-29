import sys

input = sys.stdin.readline

N, S = map(int, input().split())
p = list(map(int, input().rstrip().split()))

# 투포인터 사용
count = 100000
left = 0
right = 0

temp_sum = p[0]
while left <= right:
    if temp_sum >= S:
        count = min(count, right - left + 1)
        # 한 칸씩 줄이기
        temp_sum -= p[left]
        left += 1
    else:
        right += 1
        if right < N:
            temp_sum += p[right]
        else:
            break

if count == 100000:
    print(0)
else:
    print(count)

# 순서 변경 x
# p.sort(reverse=True)
#
# count = 0
#
# selected = p[0]
# if selected >= S:
#     count = 1
#
# j = 1
# select_count = 1
#
# while j < N:
#     if selected + p[j] >= S:
#         count = select_count + 1
#         break
#     else:
#         if j == N - 1:  # 합을 만드는 것 불가능
#             count = 0
#             break
#         selected += p[j]
#         select_count += 1
#         j += 1
#
# print(count)
