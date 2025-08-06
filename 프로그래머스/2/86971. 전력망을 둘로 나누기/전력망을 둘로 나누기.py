from collections import deque

def bfs(visited, graph, start):
    count = 1
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now_node = q.popleft()
        
        for next_node in graph[now_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                count += 1
                
    return count


def solution(n, wires):
    answer = 101
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        diff = []
        
        for j in range(len(wires)):
            if i == j:
                continue
            s, e = wires[j][0], wires[j][1]
            graph[s].append(e)
            graph[e].append(s)
        
        for k in range(1, n+1):
            if not visited[k]:
                diff.append(bfs(visited, graph, k))
                
        answer = min(answer, abs(diff[0]-diff[1]))        

    return answer