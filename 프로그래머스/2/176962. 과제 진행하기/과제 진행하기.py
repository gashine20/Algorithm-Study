def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        st = h*60+m
        plans[i][1] = st
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x:x[1])
    
    stack = []
    
    def do_Remain(remain_time): # 다음 숙제까지 남은 시간
        while stack: 
            index, remain_t = stack.pop()
            #print(plans[index], remain_t)
            remain_time -= remain_t
            if remain_time < 0: # 남은거 하다 다음 숙제 해야함
                stack.append((index, remain_time*(-1)))
                break
            else: # 끝냄
                answer.append(plans[index][0])
                #print(plans[index][0])
    
    for i in range(len(plans)):
        if i == len(plans)-1: # 마지막
            answer.append(plans[i][0])
            do_Remain(100000)
            break
        
        # 양수 : 현재 숙제 끝내기 위해 남은 시간 / 음수 : 다음 숙제까지 남은 시간
        remain_time = (plans[i][1] + plans[i][2]) - plans[i+1][1] 
        
        if remain_time > 0: # 시간이 지남
            stack.append((i, remain_time))
        elif remain_time < 0: # 숙제 다하고 남은거 함
            answer.append(plans[i][0])
            do_Remain(remain_time*(-1))
        else: # 숙제끝내고 바로 다음 숙제
            answer.append(plans[i][0])
                   
                
    return answer