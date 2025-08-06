def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    found = False
    
    def make_word(w):
        nonlocal answer, found
        
        for ch in alphabet:
            nw = w + ch
            answer+=1
            
            if nw == word:
                found = True
                return
            if len(nw) < 5:
                make_word(nw)
                if found:
                    return
            
    make_word('')
    
    
    return answer


# AAAAA (5) > AAAAE(6) > ... > E > EE > EEE > EEEE
