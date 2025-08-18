import math

def solution(n):
    answer = 0
    
    def isPrime(num):
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        
        return True
        
    for i in range(3, n+1, 2):
        if isPrime(i):
            answer += 1
            
    return answer + 1