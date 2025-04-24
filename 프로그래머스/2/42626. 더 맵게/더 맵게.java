import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int s: scoville){
            pq.offer(s);
        }
        
        int count = 0;
        while(pq.size() >= 2 && pq.peek() < K){
            int first = pq.poll();
            int second = pq.poll();
            
            int mixed = first + (second * 2);
            pq.offer(mixed);
            count++;
        }
        
        return (!pq.isEmpty() && pq.peek() >= K) ? count : -1;
    }
}