def solution(progresses, speeds):
    answer = []
    days = []
    
    for progress, speed in zip(progresses, speeds):
        day = (100-progress) // speed if (100-progress) % speed == 0 else (100-progress) // speed + 1
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