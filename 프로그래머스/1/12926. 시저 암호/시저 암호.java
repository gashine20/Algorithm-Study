import java.util.*;

class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == ' '){
                answer+=c;
            } else if (Character.isUpperCase(c)){
                int p = ((int)c - (int)('A') + n) % 26 + (int)('A');
                answer+=(char)p;
            } else if (Character.isLowerCase(c)){
                int p = ((int)c - (int)('a') + n) % 26 + (int)('a');
                answer+=(char)p;
            }
        }
        return answer;
    }
}