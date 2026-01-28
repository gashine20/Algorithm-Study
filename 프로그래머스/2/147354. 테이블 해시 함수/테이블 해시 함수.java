import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            if(o1[col-1] == o2[col-1]){
                return o2[0] - o1[0]; // col번째 값이 동일하면 첫번째 컬럼 기준 내림차순
            }
            return o1[col-1] - o2[col-1]; // col번째 기준 오름차순 
        });
        
        for(int[] d: data){
            pq.add(d);
        }
        
        int index = 1;
        while(!pq.isEmpty()){
            int[] array = pq.poll();
            // System.out.println(Arrays.toString(array));
            if(index >= row_begin && index <= row_end){
                int value = 0;
                
                for(int a: array){
                    value += (a%index);    
                }   
                // System.out.println(value);
                //XOR 연산
                answer = answer ^ value;
            }
            
            index++;
        }
        
        return answer;
    }
}