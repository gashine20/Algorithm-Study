# 회의실 배정
# 끝나는 시간을 기준으로 우선순위 큐에 삽입
# 끝나는 시간 ~ 시작 시간 맞는지 확인
from queue import PriorityQueue

N = int(input())
meetings = PriorityQueue()

for _ in range(N):
    s, e = map(int, input().split())
    meetings.put((e, s))

answer = 1
end, start = meetings.get()

while meetings.qsize() > 0:
    e, s = meetings.get()

    if s >= end:
        end = e
        answer += 1

print(answer)
