def solution(n, lost, reserve):
    answer = 0
    uniform = [1] * (n+1)
    
    for i in lost:
        uniform[i] -= 1
    for i in reserve:
        uniform[i] += 1
        
    for i in range(1, n+1):
        if uniform[i] == 2 and uniform[i-1] == 0:  
            uniform[i-1]+=1
            uniform[i] -=1
        if uniform[i] == 2 and i + 1 <= n and uniform[i+1] == 0:
            uniform[i+1]+=1
            uniform[i] -=1
    
        # print(uniform)
    
    for k in uniform[1:]:
        if k >= 1:
            answer += 1
    
    
    return answer