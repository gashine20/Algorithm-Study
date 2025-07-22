from collections import Counter

def solution(phone_book):
    answer = True
    dicts = {}
    
    
    for i in range(len(phone_book)):
        dicts[phone_book[i]] = i
    
    for i in range(len(phone_book)):
        pn_len = len(phone_book[i])
        for j in range(1, pn_len):
            if phone_book[i][:j] in dicts.keys():
                return False
        
    return answer