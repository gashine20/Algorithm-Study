import heapq as hq

def solution(operations):
    answer = []
    heap = []
    
    for operation in operations:
        op, data = operation.split()

        if op == "I":
            hq.heappush(heap, int(data))
        elif op == "D" and data == "-1" and heap: # 최솟값 추출
            hq.heappop(heap)
        elif op == "D" and data == "1" and heap: # 최대값 추출
            heap.remove(max(heap))
            hq.heapify(heap)
        
        # print(heap)
        
    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]
    
    return answer