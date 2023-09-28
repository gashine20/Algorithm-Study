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
