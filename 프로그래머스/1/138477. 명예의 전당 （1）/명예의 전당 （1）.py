from collections import deque

def solution(k, score):
    answer = []
    q = []
    
    for s in score:
        if len(q) < k:
            q.append(s)
        else:
            if q[0] < s:
                q[0] = s
                
        q.sort()
        answer.append(q[0])
        
    
    return answer