def solution(citations):
    answer = 0
    n = len(citations)
    max_value = max(citations)
    min_value = min(citations)
    
    
    for i in range(0, max_value+1):
        up = 0
        down = 0
        for citation in citations:
            if citation >= i:
                up+=1
            elif citation < i:
                down+=1
        
        if up >= i and down <= i:
            answer = i
    
    
    return answer