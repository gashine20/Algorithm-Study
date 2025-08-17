import heapq

def solution(emergency):
    answer = [0] * len(emergency)
    # 해당 환자가 몇 번째로 진료 받는지
    hall = []
    for i, e in enumerate(emergency):
        heapq.heappush(hall, (-e, i))
    
    order = 1
    while hall:
        e, i = heapq.heappop(hall)
        answer[i] = order
        order += 1
    
    return answer