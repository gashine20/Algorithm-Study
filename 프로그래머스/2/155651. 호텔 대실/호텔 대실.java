import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            return o1[0] - o2[0];
        });
        
        // 형 변환 & 정렬
        for(String[] time : book_time){
            // ["15:00", "17:00"] -> [15*60, 17*60 + 10]
            int[] t = format(time); 
            pq.offer(t);
        }
        
        PriorityQueue<Integer> finish = new PriorityQueue<>((o1, o2) -> {
            return o1 - o2;
        });
        finish.offer(23*60 + 59);
        
        // room 배정
        while (!pq.isEmpty()) {
            int[] t = pq.poll();
            System.out.println(t[0] + " -> " + t[1] );
            
            int f = finish.peek();
            
            // finish 보다 시작 시간 작으면 room ++
            if(t[0] < f){
                answer++;
            }
            else{ // finish보다 크면 빼고, room 배정x
                finish.poll();
            }
            finish.offer(t[1]);
        }
        
        
        return answer;
    }
    
    public int[] format(String[] time){
        // ["15:00", "17:00"] -> [[15,00],[17,10]]
        // ["15:00", "17:00"] -> [15*60, 17*60 + 10]
        String[] a = time[0].split(":");
        String[] b = time[1].split(":");
        
        int a1 = Integer.parseInt(a[0]) * 60 + Integer.parseInt(a[1]);
        int b1 = Integer.parseInt(b[0]) * 60 + Integer.parseInt(b[1]) + 10;
        
        
        return new int[] {a1,b1};
    }
    
    
}