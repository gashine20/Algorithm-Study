import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> { // e 오름차순, s 오름차순
            if(o1[1] == o2[1]) {
                return o1[0] - o2[0];
            }
            return o1[1] - o2[1];
        });
        for(int[] target: targets) {
            pq.offer(target);
        }
        
        int line = 0;
        while(!pq.isEmpty()) {
            int[] target = pq.poll();
            if(target[0] >= line) {
                answer++;
                // System.out.println(target[0] + 0.5);
                line = target[1];
            }
        }
        
        
        return answer;
    }
}