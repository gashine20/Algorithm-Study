import java.util.*;

class Solution {
    public int solution(int n) {
        String threeDemical = convertThreeDemical(n);
        return Integer.parseInt(threeDemical, 3);
    }
    
    public String convertThreeDemical(int n){
        StringBuilder sb = new StringBuilder();
        while(n > 0){
            sb.append(n%3);
            n /= 3;
        }
        return sb.toString();
    }
}