import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        
        // map 에 최소 index 값 넣기
        HashMap<Character, Integer> map = new HashMap<>();
        for(String key : keymap) {
            for(int i = 0; i < key.length(); i++) {
                char k = key.charAt(i);
                
                if(map.get(k) == null) { // 없으면 index + 1
                    map.put(k, map.getOrDefault(k, i) + 1);
                } else { // 있으면 최소 값 넣기
                    map.put(k, Math.min(map.get(k), i+1));
                }
            }
        }
        
        // map에서 index 찾아서 합산.
        for(int i = 0; i < targets.length; i++) {
            String target = targets[i];
            int count = 0;
            
            for(char c : target.toCharArray()){
                if (map.get(c) == null) { // map에 해당 단어 없으면 -1
                    count = -1;
                    break;
                }
                count += map.get(c);
            }
            answer[i] = count;
            
        }        
        
        
        return answer;
    }
}