def divide(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 1 + n
    for i in range(2, n//2 + 1):
        if n % i == 0:
            a += i
            
    return a

def solution(n):
    answer = divide(n)
    
    return answer