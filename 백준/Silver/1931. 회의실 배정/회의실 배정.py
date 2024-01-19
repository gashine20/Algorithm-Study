import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())

pq = PriorityQueue()
for _ in range(N):
    start, end = map(int, input().split())
    pq.put((end, start))  # 종료 시간 기준으로!

count = 0
endTime = 0

while pq.qsize() > 0:
    end, start = pq.get()

    if start >= endTime:
        # print("endTime =", endTime, "start =", start, "end =", end)

        count += 1
        endTime = end

print(count)
