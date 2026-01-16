import java.util.*;

class Solution {
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();
        
        for(char c : number.toCharArray()){
            while(sb.length() != 0 && k > 0 && sb.charAt(sb.length() - 1) < c){
                sb.deleteCharAt(sb.length()-1);
                k--;
            }
            
            sb.append(c);
        }
        // k 남아있으면 뒤에서 제거
        if (k > 0){
            sb.setLength(sb.length()-k);
        }
        
        String answer = sb.toString();
        return answer;
    }
    
    
}