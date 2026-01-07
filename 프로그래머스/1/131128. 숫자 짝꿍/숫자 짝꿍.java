import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        String result = "";
        // 3 4 0    1 3 2 0
        // 2 1 1    1 2 1 1
         
        
        
        // set으로 변환
        HashMap<String, Integer> mapX = new HashMap<>();
        HashMap<String, Integer> mapY = new HashMap<>();
        
        for (char c : X.toCharArray()) {
            String key = String.valueOf(c);
            mapX.put(key, mapX.getOrDefault(key, 0) + 1);
        }

        for (char c : Y.toCharArray()) {
            String key = String.valueOf(c);
            mapY.put(key, mapY.getOrDefault(key, 0) + 1);
        }
        
        // 비교해서 같은 개수 만큼 list에 넣어
        System.out.println(mapX.size());
        System.out.println(mapY.size());
        
        StringBuilder sb = new StringBuilder();
        
        // 정렬 대신 9 -> 0
        for (int i = 9; i >= 0; i--){
            String key = String.valueOf(i);
            int count = Math.min(
                mapX.getOrDefault(key, 0),
                mapY.getOrDefault(key, 0)
            );
            
            for(int j = 0; j < count; j++){
                sb.append(key);
            }
        }
        
        if (sb.length() == 0) return "-1";
        if (sb.charAt(0) == '0') return "0";

        return sb.toString();
    }
}