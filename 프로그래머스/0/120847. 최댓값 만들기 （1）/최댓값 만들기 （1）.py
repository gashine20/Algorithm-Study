def solution(numbers):
    answer = 0
    numbers.sort()
    
    return numbers[-1] * numbers[-2]