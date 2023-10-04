# 개수 세기 - 5m 52s

# N = int(input())
#
# num = []
#
# num = list(map(int, input().split()))
#
# v = int(input())
#
# # count = 0
# # for n in num:  # 같은 것이 있으면 count 1씩 증가
# #     if n == v:
# #         count += 1
# #
# # print(count)
#
# print(num.count(v))

# X보다 작은 수 - 3m 12s
# X보다 작은 수를 A에서 찾아라
#
# N, X = list(map(int, input().split()))
# A = list(map(int, input().split()))
#
# count = []
# for a in A:
#     if a < X:
#         count.append(a)
#
# for c in count:
#     print(c, end=' ')

# 최소, 최대 - 1m 50s
# N = int(input())
# num = list(map(int,input().split()))
#
# print(min(num), max(num))

# 공 넣기 - 11m
# N 바구니 개수, M번 공을 넣음
# N, M = map(int, input().split())
#
# bucket = [0] * (N + 1)  # 배열 크기 지정 ! ! !
#
# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for p in range(i, j + 1):  # i~j k번호 적혀있는 공을 넣음
#         bucket[p] = k  # -> index out of range 오류 뜸
#
# for i in range(1, len(bucket)):  # 처음 바구니는 [0] 비어 있음
#     print(bucket[i], end=' ')

# 공 바꾸기 - 5m 46s
# N 바구니 개수, M번 바꿈
# N, M = map(int, input().split())
#
# bucket = [0] * (N + 1)  # 0으로 채워줘야
# for i in range(1, len(bucket)):
#     bucket[i] = i
#
# for _ in range(M):
#     i, j = map(int, input().split())
#     tmp = bucket[i]
#     bucket[i] = bucket[j]
#     bucket[j] = tmp
#
# for i in range(1, len(bucket)):
#     print(bucket[i], end=' ')

# 과제 안 내신 분..? - 5m 21s
# bucket = [0] * 31
# for _ in range(28):
#     bucket[int(input())] = 1
#
# #print(bucket)
#
# for i in range(1, 31):
#     if bucket[i] == 0:
#         print(i)

# 나머지 - 3m 25s
# remain = []
# for _ in range(10):
#     r = int(input()) % 42
#     if r not in remain: # 배열에 없으면 넣어라
#         remain.append(r)
#
# print(len(remain)) # 배열 길이 return

# 바구니 뒤집기 - 16m 안됨 ㅠㅠ -> Index 잘못 설정
# N 바구니의 개수, M 번 바구니의 순서를 역순으로

N, M = map(int, input().split())

# baskets = [0] * (N + 1)
# baskets_same = [0] * (N + 1)

# for i in range(1, len(baskets)):
#     baskets[i] = i
#     # baskets_same[i] = i
# 이렇게 바꿀 수 있음
baskets = [i for i in range(1, N + 1)]  # [1, 2, 3, 4, 5]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = baskets[i - 1:j]  # basket[0:4] -> 1~4
    tmp.reverse()
    baskets[i - 1:j] = tmp

    # index = j
    # for k in range(i, j + 1):  # 3~4
    #     baskets_same[index] = baskets[k]  # 4->3이 되고, 3->4가 됨
    #     index -= 1

    # buckets = baskets_same

# for i in range(1, len(basket)):
#     print(basket[i], end=' ')
for basket in baskets:
    print(basket, end=' ')

# 평균 - 6m 13s
# N = int(input())
#
# scores = list(map(int, input().split()))
#
# max_score = max(scores)
#
# sum_score = 0
# for score in scores:
#     sum_score += (score / max_score) * 100
#
# print(sum_score / N)
