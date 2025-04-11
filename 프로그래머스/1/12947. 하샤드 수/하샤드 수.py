def solution(x):
    answer = x % sum([int(num) for num in str(x)]) == 0
    
    return answer