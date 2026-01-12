import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int[] point = {0,3,2,1,0,1,2,3};
        HashMap<String, Integer> map = new HashMap<>();
        
        // 점수 매기기
        for(int i = 0; i < survey.length; i++){
            String[] option = survey[i].split(""); // ["A", "N"]
            if(choices[i] < 4) {
                map.put(option[0], map.getOrDefault(option[0], 0)+point[choices[i]]);
            } else if (choices[i] > 4) {
                map.put(option[1], map.getOrDefault(option[1], 0)+point[choices[i]]);
            }
        }
        
        // 유형 정하기
        String[] styles = {"RT", "CF", "JM", "AN"}; // 사전순
        
        for(String style : styles){
            String[] s = style.split("");
            
            int a = map.getOrDefault(s[0], 0);
            int b = map.getOrDefault(s[1], 0);
            
            if(a < b){
                answer += s[1];
            } else {
                answer += s[0];
            }
        }
        
        
        return answer;
    }
}