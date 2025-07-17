import java.util.*;

class Solution {
    List<String> result = new ArrayList<>();
    boolean[] used;
    
    public String[] solution(String[][] tickets) {
        int n = tickets.length;
        Arrays.sort(tickets, (a, b) -> a[1].compareTo(b[1]));

        used = new boolean[n];        
        dfs("ICN", "ICN", tickets, 0);
        
        return result.get(0).split(" ");
    }
    
    public void dfs(String current, String path, String[][] tickets, int count){
        if(tickets.length == count){
            result.add(path);
            return;
        }
        
        for(int i = 0; i < tickets.length; i++){
            if(!used[i] && tickets[i][0].equals(current)){
                used[i] = true;
                dfs(tickets[i][1], path + " " + tickets[i][1], tickets, count+1);
                used[i] = false;
            }
        }
    }
}