def solution(t, p):
    answer = 0
    k = len(p)
    
    for i in range(len(t)-k+1):
        a = int(t[i:i+k])
        if a <= int(p):
            answer+=1
    
    return answer