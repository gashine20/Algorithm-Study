import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        
        int index = 0;
        int totalWeight = 0;
        for(int i = 0; i < bridge_length; i++){
            queue.add(0); // bridge_length 만큼 queue에 0 add
        }
        
        while(!queue.isEmpty()){
            answer++;
            
            int exited = queue.poll();
            totalWeight -= exited;
            
            if (index < truck_weights.length) {
                if (totalWeight + truck_weights[index] <= weight) {
                    totalWeight += truck_weights[index];
                    queue.add(truck_weights[index++]);
                } else {
                    queue.add(0);
                }
            }
            
        }
        
        
        return answer;
    }
}