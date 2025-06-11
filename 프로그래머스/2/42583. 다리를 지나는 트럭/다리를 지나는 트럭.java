import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        
        int index = 0;
        int totalWeight = truck_weights[index];
        queue.add(truck_weights[index++]);
        
        while(totalWeight != 0){
            answer+=1;
            
            if(queue.size() == bridge_length){ // 다리를 지난 트럭 꺼내기
                int now = queue.poll();
                totalWeight -= now;
            }
            
            if(index < truck_weights.length && totalWeight + truck_weights[index] <= weight){ // 최대 길이보다 작고, 최대 무게보다 작은 경우
                if(queue.size() < bridge_length){
                    totalWeight += truck_weights[index];
                    queue.add(truck_weights[index++]);
                }
            } else {
                if(queue.size() < bridge_length){
                    queue.add(0);
                }
            }
            
        }
        
        
        return answer+1;
    }
}