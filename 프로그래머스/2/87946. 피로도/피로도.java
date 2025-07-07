import java.util.*;

class Solution {
    int answer = -1;
    
    public int solution(int k, int[][] dungeons) {

        boolean[] visited = new boolean[dungeons.length];
        int cnt = 0;
        
        dfs(k, dungeons, visited, cnt);
        
        return answer;
    }
    
    public void dfs(int k, int[][] dungeons, boolean[] visited, int cnt){
        for(int i = 0; i < dungeons.length; i++){
            if(!visited[i] && k >= dungeons[i][0]){
                visited[i] = true;
                dfs(k-dungeons[i][1], dungeons, visited, cnt+1);
                visited[i] = false;
            }
        }
        answer = Math.max(answer, cnt);
    }
}