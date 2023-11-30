from collections import deque

N, L = map(int, input().split())

A = list(map(int, input().split(' ')))

# deque 사용
mydeque = deque()

for i in range(N):
    # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거 - pop()
    while mydeque and mydeque[-1][0] > A[i]:
        mydeque.pop()
    # 덱의 마지막 위치에 현재 값 저장 - append()
    mydeque.append((A[i], i))
    # 덱의 1번째 위치에서부터 L의 범위를 벗어난 값 덱에서 제거
    if mydeque[0][1] <= i - L:
        mydeque.popleft()

    #print(mydeque)
    # 덱의 1번째 데이터 출력 - popleft()
    print(mydeque[0][0], end=" ")



# 내 풀이 - 시간 초과 ㅎㅎ
# D = []
# for i in range(N): # 0~11
#     bridge = []
#     for j in range(L): # 0, 1, 2
#         if i - j >= 0:
#             bridge.append(A[i - j])
#     #print(bridge)
#     D.append(min(bridge))
#
# for d in D:
#     print(d, end=" ")
