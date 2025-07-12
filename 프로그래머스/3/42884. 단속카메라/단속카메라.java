import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> Integer.compare(a[1], b[1]));
        
        for(int[] route : routes){
            pq.offer(route);
        }
        
        int[] now = pq.poll();
        int end = now[1];
        
        while(pq.size() > 0){
            int[] next = pq.poll();
            int nextStart = next[0];
            
            if(nextStart > end){
                //System.out.println(end);
                answer++;
                end = next[1];
                //System.out.println(end + "으로 바뀜");
            }
            if(pq.size() == 0){ // 마지막엔 answer+1
                answer++;
            }
        }
        
        return answer;
    }
}