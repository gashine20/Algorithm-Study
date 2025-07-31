import math

def solution(numbers):
    def isPrime(num):
        num = int(num)
        
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True
        
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        
        return True
    
    numbers_list = [n for n in numbers]
    print(numbers_list)
    n = len(numbers_list)
    used = [False] * n
    
    # 백트래킹
    result = set()
    
    def makeNumber(current):
        if current:
            if isPrime(current):
                result.add(int(current))
        
        for i in range(n):
            if not used[i]:
                used[i] = True
                makeNumber(current+numbers_list[i])
                used[i] = False
            
    
    makeNumber('')
    
    return len(result)