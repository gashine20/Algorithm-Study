import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100-progress) / speed)
        days.append(day)
        
    before = days[0]
    count = 0
    for day in days:
        if before >= day:
            count+=1
        else:
            answer.append(count)
            count = 1
            before = day
    # 마지막 값 넣기
    answer.append(count)
    
    return answer