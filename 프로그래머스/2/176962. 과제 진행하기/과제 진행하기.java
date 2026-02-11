import java.util.*;

class Solution {
    public String[] solution(String[][] plans) {
        int n = plans.length;
        String[] answer = new String[n];
        
        // PriorityQueue에 o[1] 기준으로 오름차순 
        PriorityQueue<String[]> pq = new PriorityQueue<>((o1, o2) -> {
            String[] time = o1[1].split(":");
            String[] time2 = o2[1].split(":");
            
            int t1 = Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
            int t2 = Integer.parseInt(time2[0]) * 60 + Integer.parseInt(time2[1]);
            return t1 - t2;
        });
        
        for(String[] plan : plans) {
            pq.offer(plan);
        }
        
        int index = 0;
        Stack<String[]> stack = new Stack<>(); // 중단된 과제 넣는 곳
        String[] now = pq.poll();
        
        while(!pq.isEmpty()) {
            String[] next = pq.poll();
            // System.out.println("now: " + Arrays.toString(now) + " next:" + Arrays.toString(next));
            
            int now_time = calcTime(now[1]);
            int next_time = calcTime(next[1]);
            int diff = next_time - now_time;
            
            int cost = Integer.parseInt(now[2]);
            if(cost > diff) { // 중단
                String remain = Integer.toString(cost - diff);
                stack.push(new String[]{now[0], now[1], remain}); // 남은 시간 push
            } else if (cost == diff) { // 딱 맞게 끝남
                answer[index++] = now[0];
            } else { // cost < diff now 끝나고 next하기까지 시간이 남음
                answer[index++] = now[0];
                
                int remain = diff -cost; // 다음까지 시간
                while(!stack.isEmpty()) {
                    if(remain <= 0) break;
                    String[] s = stack.pop(); // 12:30 90
                    int c = Integer.parseInt(s[2]);
                    if(remain >= c) { // 다음까지 시간 > 남은시간 = answer
                        answer[index++] = s[0];
                    } else { // 다시 stack에 
                        stack.push(new String[]{s[0], s[1], Integer.toString(c-remain)});
                    }
                    remain -= c;
                }
            
            }
            now = next;
            
        }
        // 마지막꺼 넣기
        answer[index++] = now[0];
        
        // stack에 중단된 것들 있으면 넣기
        while(!stack.isEmpty()) {
            String[] s = stack.pop();
            answer[index++] = s[0]; 
        }
        
        
        return answer;
    }
    
    public int calcTime(String time) {
        String[] t = time.split(":");
        
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
}