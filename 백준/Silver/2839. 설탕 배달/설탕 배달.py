N = int(input())

bag = 0

# 3을 먼저 빼고 5를 나눈다.
while N > 0:
    if N % 5 == 0:
        bag += (N // 5)
        break
    N -= 3
    bag += 1

if N < 0:
    bag = -1

print(bag)

# 5을 나누고 3을 뺀다 풀이.. - 오답
# 1
# a = 1000
# b = 0
#
# # 1
# if N % 5 == 0:
#     a = N // 5
# elif N % 3 == 0:
#     a = N // 3
# #print("a", a)
#
# # 2
# while N > 0:
#     N -= 5
#     b += 1
#
#     # print("N", N)
#     if N % 3 == 0:
#         break
#
# #print("b", b)
# if N < 0: # 2번 진행
#     if a == 1000:# 1번 진행 안했을 때
#         bag = -1
#     else:
#         bag = a
# else: # N>=0 이면 3으로 나누어떨어져서 break 한거니까
#     #print("남은 N:", N)
#     b += N // 3
#     bag = min(a, b)
#
# print(bag)
