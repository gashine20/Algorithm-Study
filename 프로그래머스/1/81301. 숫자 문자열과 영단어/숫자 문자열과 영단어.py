def solution(s):
    answer = ''
    
    number_alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    number = ''
    for alpha in s:
        if alpha.isdigit():
            answer += alpha
        else: # 문자이면
            number += alpha
            
        if number in number_alpha:
            answer += str(number_alpha.index(number))
            number = ''
            
    return int(answer)
    