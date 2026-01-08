import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<>();
        
        int[] result = new int[progresses.length];
        
        for(int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i];
            int done = (remain % speeds[i] != 0) ? (remain / speeds[i]) + 1 : (remain / speeds[i]);
            result[i] = done;
        }
        
        int line = result[0];
        int count = 0;
        for(int i = 0; i < result.length; i++){
            if(line < result[i]) {
                list.add(count);
                line = result[i];
                count = 1; // 초기화
            } else{
                count += 1;
            }
        }
        
        // 마지막 넣기
        list.add(count);
        
        // list -> array
        int[] answer = list.stream()
            .mapToInt(Integer::intValue)
            .toArray();
        

        return answer;
    }
}