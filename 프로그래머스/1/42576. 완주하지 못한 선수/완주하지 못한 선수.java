import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String people : participant){
            map.put(people, map.getOrDefault(people, 0) + 1);
        }
        
        for(String people : completion){
            map.put(people, map.get(people) - 1);
        }
        
        for(String people : map.keySet()){
            if(map.get(people) != 0) {
                return people;
            }
        }
        
        return answer;
    }
}