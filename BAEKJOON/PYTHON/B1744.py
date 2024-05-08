# 수 묶기

from queue import PriorityQueue

N = int(input())
zeroCount = 0
oneCount = 0
mqueue = PriorityQueue()
pqueue = PriorityQueue()

for _ in range(N):
    a = int(input())

    if a < 0:
        mqueue.put(a)
    elif a > 1:
        pqueue.put(a * (-1))
    elif a == 0:
        zeroCount += 1
    elif a == 1:
        oneCount += 1

answer = 0
# minus
while mqueue.qsize() > 1:
    a = mqueue.get()
    b = mqueue.get()
    answer += a * b

if mqueue.qsize() == 1 and zeroCount == 0:
    answer += mqueue.get()

# plus
while pqueue.qsize() > 1:
    a = pqueue.get()
    b = pqueue.get()
    answer += a * b

if pqueue.qsize() == 1:
    answer += pqueue.get() * (-1)

# 1 처리
answer += oneCount

print(answer)
