def solution(a, b):
    answer = ''
    last_date = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    period = 0
    for i in range(a-1):
        period += last_date[i]
        
    period += b - 1
    remain = period % 7
    
    return date[(5 + remain) % 7]



# 1월 1일 금
# 1월 4일 월
# 1월 8일 금
# 1월 6일 수 (6-1) % 7 = 5 => Fri + 3

# 2월 1일 : 1월 1일 = 1 2월 1일 = (31 + 1 - 1)일 째, 31 % 7 = 3, fri + 3 = "MON"