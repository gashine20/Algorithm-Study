import heapq

def solution(emergency):
    answer = []
    emergency_copy = emergency[:]
    emergency_copy.sort(reverse=True)
    
    for i in range(len(emergency)):
        answer.append(emergency_copy.index(emergency[i])+1)
    
    return answer