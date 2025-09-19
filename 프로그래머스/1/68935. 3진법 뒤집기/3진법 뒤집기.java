import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        String threeDemical = convertThreeDemical(n);
        for(int i = 0; i < threeDemical.length(); i++){
            answer += Character.getNumericValue(threeDemical.charAt(i)) * Math.pow(3, i);
        }
        
        return answer;
    }
    
    public String convertThreeDemical(int n){
        StringBuilder sb = new StringBuilder();
        while(n > 0){
            sb.append(n%3);
            n /= 3;
        }
        return sb.reverse().toString();
    }
}