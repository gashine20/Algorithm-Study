import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < players.length; i++){
            map.put(players[i], i);
        }
        
        for(String calling : callings) {
            // switch
            int callIndex = map.get(calling); // O(1)
            String beforePlayer = players[callIndex-1];
            players[callIndex-1] = calling;
            players[callIndex] = beforePlayer;
            
            // map 갱신
            map.put(calling, callIndex-1);
            map.put(beforePlayer, callIndex);
        }
        
        return players;
    }
}