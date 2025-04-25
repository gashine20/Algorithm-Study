import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minPq = new PriorityQueue<>(); // 오름차순
        PriorityQueue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder()); // 내림 차순
        
        for(String op : operations){
            String[] array = op.split(" ");
            
            if(array[0].equals("I")){
                int num = Integer.parseInt(array[1]); // String -> int
                minPq.offer(num);
                maxPq.offer(num);
            } else{
                if(maxPq.isEmpty() && minPq.isEmpty()) {continue;}
                else {
                    if(array[1].equals("1")){ // 최댓값 삭제
                        int max = maxPq.poll();
                        minPq.remove(max);
                    } else if(array[1].equals("-1")){ // 최솟값 삭제
                        int min = minPq.poll();
                        maxPq.remove(min);
                    }
                }
            } 
        }
        
        int[] answer = new int[2];
        if(minPq.isEmpty() && maxPq.isEmpty()){
            answer[0] = 0;
            answer[1] = 0;
        } else {
            answer[0] = maxPq.peek();
            answer[1] = minPq.peek();
        }
        
        
        return answer;
    }
}