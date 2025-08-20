def solution(t,p):
    answer = 0
    n, k= len(t), len(p) 
    
    for i in range(n-k+1):
        if int(t[i: i+k]) <= int(p):
            answer += 1
            
    return answer
