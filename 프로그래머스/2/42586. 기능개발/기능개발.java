import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> result = new ArrayList<>();
        
        int[] time = new int[progresses.length];
        for(int i = 0 ; i < time.length; i++){
            time[i] = (100 - progresses[i]) / speeds[i];
            if((100 - progresses[i]) % speeds[i] != 0){
                time[i] += 1;
            }
        }
        
        int compare = time[0];
        int count = 1;
        
        for(int i = 1; i < time.length; i++){
            if(compare >= time[i]){
                count += 1;
            } else{
                result.add(count);
                count = 1;
                compare = time[i];
            }
        }
        result.add(count); // 마지막에 count 넣음
        
        int[] answer = result.stream().mapToInt(i -> i).toArray();
        
        
        return answer;
    }
}