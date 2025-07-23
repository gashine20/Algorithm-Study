def solution(s):
    answer = True
    
    before = s[0]
    s_count = 0
    for s_type in s:
        if s_type == "(":
            if before == ")" and s_count < 0:
                return False
            s_count += 1
        elif s_type == ")":
            s_count -= 1
        before = s_type
    
    if s_count != 0:
        return False
    
    return True