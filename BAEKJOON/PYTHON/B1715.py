# 카드 정렬하기
from queue import PriorityQueue

N = int(input())
myqueue = PriorityQueue()

for _ in range(N):
    myqueue.put(int(input()))

sum = 0
answer = 0

while myqueue.qsize() > 0:
    a = myqueue.get()
    b = myqueue.get()
    sum = a + b
    answer += sum
    # print("a =", a, "b =", b, "sum =", sum)
    if not myqueue.empty():
        myqueue.put(sum)

print(answer)
