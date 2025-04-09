def solution(n):
    answer = ''
    a = list(map(int, str(n)))
    a.sort(reverse=True)
    
    for num in a:
        answer += str(num)
    answer = int(answer)
    
    
    
    return answer