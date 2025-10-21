import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        // dict 생성
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            
            if(map.containsKey(c)){
                answer[i] = i - map.get(c);
            } else {
                answer[i] = -1;
                map.put(c, i);
            }
            map.put(c, i);
        }

        return answer;
    }
}