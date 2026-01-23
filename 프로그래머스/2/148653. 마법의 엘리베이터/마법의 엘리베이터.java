import java.util.*;

class Solution {
    public int solution(int storey) {
        ArrayList<Integer> result = new ArrayList<>();
        dfs(storey, 0, result);
        
        int answer = 0;
        Collections.sort(result);
        if(!result.isEmpty()) {
            answer =  result.get(0);
        }
        
        return answer;
    }
    
    
    public void dfs(int storey, int count, ArrayList<Integer> result){
        if(count >= 1000) return;
        
        if(storey == 0){
            result.add(count);
            return;
        }
        
        int digit = storey % 10;
        dfs(storey/10, count + digit, result);
        dfs(storey / 10 + 1, count + (10-digit),result);
    }
}