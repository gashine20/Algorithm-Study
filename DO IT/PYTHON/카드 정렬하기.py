import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
pq = PriorityQueue()

for _ in range(N):
    pq.put(int(input()))

sum = 0
while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    sum += temp
    # print(data1, "+", data2, "=", temp)
    pq.put(temp)

print(sum)
