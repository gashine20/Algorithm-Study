import math

def solution(n):
    answer = 0
    
    a = int(math.sqrt(n))
    if a**2 == n:
        answer = (a+1)**2
    else:
        answer = -1
    
    return answer