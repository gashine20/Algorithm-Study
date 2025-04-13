def solution(price, money, count):
    total = 0
    for i in range(1, count+1):
        total += price * i
    
    answer = total - money if money < total else 0
    
    
    return answer