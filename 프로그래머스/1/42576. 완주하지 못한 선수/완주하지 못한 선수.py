def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i] :
            return participant[i]
        
    #마지막 주자
    return participant[len(participant)-1]

    