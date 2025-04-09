def solution(s):
    answer = True
    
    s = s.lower()
    countP = 0
    countY = 0
    
    for alph in s:
        if alph == 'p':
            countP +=1
        elif alph == 'y':
            countY +=1
            
    if countP != countY:
        answer = False
    
    return answer