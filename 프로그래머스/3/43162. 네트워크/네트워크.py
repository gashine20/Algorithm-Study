from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    mydeque = deque()
    
    for i in range(n):
        if not visited[i]:
            mydeque.append(i)
            visited[i] == True
            
            while mydeque:
                now = mydeque.popleft()

                for i in range(len(computers[now])):
                    if computers[now][i] == 1:
                        if not visited[i]:
                            visited[i] = True
                            mydeque.append(i)
            answer+=1
        
        # print(visited)

    return answer