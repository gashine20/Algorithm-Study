from queue import PriorityQueue

def solution(scoville, K):
    answer = 0
    pq = PriorityQueue()
    for s in scoville:
        pq.put(s)
    
    while True:
        first = pq.get()
        if first >= K:
            break
        if first < K and pq.qsize() <= 0:
            answer = -1
            break
            
        second = pq.get()
        pq.put(first + (second * 2))
        answer+=1
    
    return answer