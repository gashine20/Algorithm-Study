import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        // s 모두 소문자로 변경
        String sen = s.toLowerCase();
        // s에 'p'의 개수와 'y'의 개수를 비교
        int p = 0;
        int y = 0;
        for(int i = 0; i < sen.length(); i++){
            if(sen.charAt(i) == 'p'){
                p+=1;
            }
            if(sen.charAt(i) == 'y'){
                y+=1;
            }
        }
            
        // 같으면 true, 다르면 false,
        if(p != y){
            answer = false;
        }

        return answer;
    }
}