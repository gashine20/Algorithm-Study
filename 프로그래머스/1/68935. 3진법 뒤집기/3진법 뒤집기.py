def solution(n):
    answer = 0
    list_3nd = []
    
    while n:
        remain = n % 3
        list_3nd.append(remain)
        n //= 3
        
    for i in range(len(list_3nd)):
        answer += list_3nd[i] * 3**(len(list_3nd)-i-1)
        
    return answer