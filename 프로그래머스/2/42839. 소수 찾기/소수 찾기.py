from itertools import permutations
import math

def solution(numbers):
    answer = 0
    
    def is_prime(num):
        if num == 0 or num == 1: return False
        if num == 2 : return True
            
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0: return False
        
        return True
    
    numbers = list(numbers)
    number_set = set()
    
    for i in range(1, len(numbers)+1):
        for number in permutations(numbers,i):
            num = ''.join(number)
            number_set.add(int(num))
    
    answer = [n for n in list(number_set) if is_prime(n)]
    
    return len(answer)