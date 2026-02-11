import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = -1;
        
        // 맞춰야하는 큐 원소 합
        long q1_sum = Arrays.stream(queue1).sum();
        long q2_sum = Arrays.stream(queue2).sum();
        long total = q1_sum + q2_sum;
        
        // 홀수면 -1 
        if(total % 2 != 0) {
            return -1;
        }
        total = total/2;
        
        // queue에 넣기
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        for(int q : queue1) {
            q1.offer(q);
        }
        for(int q : queue2) {
            q2.offer(q);
        }
        
        // 32724 (18) 651(12)
        // 2724(15) 651(15)
        
        int n = (queue1.length + queue2.length) * 3; // 최대 움직일 수 있는
        int count = 0;
        while(count <= n) {
            if(q1_sum == total && q2_sum == total) {
                answer = count;
                break;
            }
            
            if(q1_sum < q2_sum && !q2.isEmpty()) { // q2에서 q1로 넘겨줌
                int a = q2.poll();
                q1.offer(a);
                q1_sum += a;
                q2_sum -= a;
            } else if (q1_sum > q2_sum && !q1.isEmpty()) { // q1 에서 q2로 넘겨줌
                int a = q1.poll();
                q2.offer(a);
                q1_sum -= a;
                q2_sum += a;
            }
            // System.out.println(q1 + " " + q2);
            count++;
        }
        
        return answer;
    }
    
}