from queue import PriorityQueue

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    pq = PriorityQueue()
    
    for s, e, w in costs:
        pq.put((w,s,e))
    
    
    def find(a):
        if a == parent[a]:
            return parent[a]
        else:
            parent[a] = find(parent[a])
            return parent[a]
    
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[b] = a
    
    useEdge = 0
    while useEdge < n-1:
        w, a, b = pq.get()
        if find(a) != find(b):
            union(a, b)
            answer += w
            useEdge += 1
    
    return answer