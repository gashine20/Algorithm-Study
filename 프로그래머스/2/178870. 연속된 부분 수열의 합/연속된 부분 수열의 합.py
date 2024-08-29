def solution(sequence, k):
    l = 0
    r = 0
    n = len(sequence)
    total_sum = sequence[0]
    
    answer = [0, n]
    
    while True:
        #print("l =", l, "r =", r, "total_sum =", total_sum)

        
        if total_sum < k:
            r+=1
            if r == n: 
                break
            total_sum += sequence[r]
        else:
            if total_sum == k:
                if r-l < answer[1] - answer[0]:
                    answer = [l, r]
            total_sum -= sequence[l]
            l+=1
    
    return answer