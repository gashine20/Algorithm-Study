import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        ArrayList<Integer> result = new ArrayList<>();
        Queue<int[]> queue = new LinkedList<>();
        int len = prices.length;
        
        // (1,1),(2,2),(3,3),(4,2),(5,3),(5,0)
        for(int i = 0; i < len; i++){
            int[] array = new int[2];
            array[0] = i + 1;
            array[1] = prices[i];
            queue.add(array);
        }
        int[] array = new int[2];
        array[0] = len;
        array[1] = 0;
        queue.add(array);
        
        while(!queue.isEmpty()){
            int[] now = queue.poll();
            
            for(int[] next: queue){
                if(now[1] > next[1]){
                    result.add(next[0]-now[0]);
                    break;
                }
            }
        }
        
        int[] answer = result.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}