import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        int num = -1;
        ArrayList<Integer> result = new ArrayList<>();
        
        for(int number: arr){
            if(num!= number){
                result.add(number);
                num = number;
            }
        }
        
        int[] answer = new int[result.size()];
        for(int i = 0; i < result.size(); i++){
            answer[i] = result.get(i);
        }
        
        
        return answer;
    }
}