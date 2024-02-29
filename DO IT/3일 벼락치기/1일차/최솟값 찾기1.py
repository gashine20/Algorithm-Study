import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
A = list(map(int, input().split()))

mydeque = deque()

for i in range(n):
    # 뒤에서 부터 현재꺼 보다 크면
    while mydeque and mydeque[-1][1] > A[i]:
        mydeque.pop()
    mydeque.append((i, A[i]))

    # 범위 확인
    if mydeque[0][0] < i - l + 1:
        mydeque.popleft()

    print(mydeque[0][1], end=" ")
