import sys

input = sys.stdin.readline

N, K = map(int, input().split())
use = list(map(int, input().split()))

# 우선순위로 계산
code = []
answer = 0

# 초기화
for this in range(K):
    if use[this] in code:
        continue

    if len(code) < N:  # 코드 자리 남음
        code.append(use[this])
        continue

    priority = []
    for c in code:
        if c in use[this:]:  # 다음에 또 이용해야 한다면!!!
            priority.append(use[this:].index(c))  # 우선순의에 다음에 또 이용될 물건의 index 값을 저장
        else:
            priority.append(101)

    target = priority.index(max(priority))  # 우선순위가 가장 높은 애가 교체될 예정
    code.remove(code[target])
    code.append(use[this])
    answer += 1

print(answer)

#
# tab = [0] * N
# check = [False] * N
#
# # 초기 설정
# for i in range(N):
#     tab[i] = use[i]
# 3 9
# 1 2 3 4 1 1 2 2 1 인 경우 성립x
# for i in range(N, len(use)):
#     # print("Tab", tab)
#
#     if use[i] in tab:
#         continue
#
#     if i + N - 1 < len(use):
#         # print("D")
#         for j in range(i + 1, i + N):
#             if use[j] in tab:
#                 idx = tab.index(use[j])
#                 check[idx] = True  # 뒤에 있다고 확인
#     else:
#         for j in range(i, len(use)):
#             if use[j] in tab:
#                 idx = tab.index(use[j])
#                 check[idx] = True  # 뒤에 있다고 확인
#
#     # print(check)
#     for k in range(len(check)):
#         if not check[k]:  # 다음에 안나온다면
#
#             # print("뒤에 안나옴 : ", use[k], tab[k], "<->", use[i])
#             tab[k] = use[i]  # 현재 아이를 tab에 넣음
#             change_count += 1
#             break
#
#     # 다시 초기화
#     check = [False] * N


# print(change_count)
