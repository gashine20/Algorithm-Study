def solution(a, b, n):
    answer = 0
    
    remain = 0
    while n >= a:
        get = b * (n// a)
        answer += get
        n = n - a * (n//a) + get
        
    return answer