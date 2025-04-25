import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for(int[] command: commands){
            int i = command[0];
            int j = command[1];
            int k = command[2];
            
            ArrayList<Integer> list = new ArrayList<>();
            for(int p = i-1; p < j; p++){
                list.add(array[p]);
            }
            Collections.sort(list);
            result.add(list.get(k-1));
        }
        
        int[] answer = result.stream().mapToInt(x -> x).toArray();
        
        return answer;
    }
}