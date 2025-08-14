def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    
    def dfs(result, index):
        nonlocal answer
        
        if index == n and result == target:
            answer +=1
            
        if index < n:
            dfs(result+numbers[index], index +1)
            dfs(result-numbers[index], index +1)
    
    dfs(0, 0)
    
    return answer