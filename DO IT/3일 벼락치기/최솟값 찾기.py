import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

A = list(map(int, input().split()))
mydeque = deque()

for i in range(n):
    # 끝에 있는 값이 넣으려고 하는 index 2보다 크면 빼기
    while mydeque and mydeque[-1][1] > A[i]:
        mydeque.pop()
    mydeque.append((i, A[i]))
    # 앞에 있는 값의 index가 범위를 벗어나면
    if mydeque[0][0] <= i - l:
        mydeque.popleft()

    print(mydeque[0][1], end=" ")
