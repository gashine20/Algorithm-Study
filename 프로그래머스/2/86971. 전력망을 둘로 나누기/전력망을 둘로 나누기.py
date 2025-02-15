from collections import deque
import sys

def bfs(start, visited, graph):
    queue = deque()
    visited[start] = True
    queue.append(start)

    count = 0
    while queue:
        now = queue.popleft()
        count += 1
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    return count


def solution(n, wires):
    answer = 100
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for wire in wires: # graph 초기화
        s = wire[0]
        e = wire[1]
        graph[s].append(e)
        graph[e].append(s)
    
    for wire in wires: # graph 하나씩 빼기
        s = wire[0]
        e = wire[1]
        index1 = graph[s].index(e)
        index2 = graph[e].index(s)
        graph[s].pop(index1)
        graph[e].pop(index2)
        
        count = []
        for i in range(1, n+1):
            if not visited[i]:
                value = bfs(i, visited, graph)
                count.append(value)
        
        answer = min(answer, max(count) - min(count))
        
        graph[s].append(e)
        graph[e].append(s)
        visited = [False] * (n+1)
        
    return answer