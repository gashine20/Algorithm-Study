import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {        
        // 무적권 적절한 시기에 사용해서 최대한 많은 라운드 진출
        // 무적권 -> 가장 많을 때 써야하지 않나
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder()); // 내림차순
        
        int round = 0;
        for(int i = 0; i < enemy.length; i++) {
            n -= enemy[i];
            pq.add(enemy[i]);
            
            if(n < 0) { // 병사 부족
                if(k > 0) { // 무족권 있으면
                    n+=pq.poll();
                    k--;
                } else {
                    break;
                }
            }
            round++;
        }
        
        return round;
    }
}