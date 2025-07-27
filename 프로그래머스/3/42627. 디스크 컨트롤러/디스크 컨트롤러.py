from collections import deque
import heapq as hq

def solution(jobs):
    answer = 0 # 반환시각 - 요청시각
    time = 0
    heap = []
    index = 0
    
    jobs.sort()
    
    for i in range(len(jobs)):
        if jobs[i][0] == time:
            hq.heappush(heap, (jobs[i][1], jobs[i][0], i)) # 소요시간, 요청시각, 작업 번호
            index = i + 1
        else:
            break
    
    while index < len(jobs) or len(heap) > 0:
        if len(heap) > 0:
            clear_job = hq.heappop(heap)
            time += clear_job[0]
            # print("time:", time, "clear_job:", clear_job)
            answer += time - clear_job[1]

        # 현재 시간에 맞춰 들어온 작업 heap에 넣기
        while index < len(jobs):
            job = jobs[index]
            if(job[0] <= time):
                hq.heappush(heap, (job[1], job[0], index))
                index+=1
            else:
                break
        
        if len(heap) == 0:
            time += 1
                
    return answer // len(jobs)