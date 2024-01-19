import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
minusPq = PriorityQueue()
plusPq = PriorityQueue()
one = 0
zero = 0

for _ in range(N):
    a = int(input())  # 수정된 부분: strip()으로 공백 제거
    if a > 1:
        plusPq.put(a * -1)
    elif a == 1:
        one += 1
    elif a == 0:
        zero += 1
    else:
        minusPq.put(a)

sum = 0
# 양수
while plusPq.qsize() > 1:
    data1 = plusPq.get() * (-1)
    data2 = plusPq.get() * (-1)
    sum += data1 * data2

if plusPq.qsize() > 0:
    sum += plusPq.get() * (-1)

# 음수
while minusPq.qsize() > 1:
    data1 = minusPq.get()
    data2 = minusPq.get()
    sum += data1 * data2

if minusPq.qsize() > 0:  # 하나 남았으면, 0이랑 곱해서 0 만듬
    if zero == 0:  # 0이 없다면 minus도 더하기
        sum += minusPq.get()

sum += one

print(sum)
