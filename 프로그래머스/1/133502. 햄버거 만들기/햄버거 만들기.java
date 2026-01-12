import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        String hamburger = "1231";
        StringBuilder result = new StringBuilder();
        
        for(int i : ingredient) {
            result.append(i);
            // System.out.println(result);
            
            if(result.length() > 3) {
                if(result.substring(result.length()-4,result.length()).equals(hamburger)){
                    answer++;
                    result.delete(result.length()-4,result.length());
                }
            }
        }
        
        
        
        
        
        return answer;
    }
}