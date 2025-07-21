import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        boolean[][] graph = new boolean[n+1][n+1];
        
        for(int[] result: results){
            int win = result[0];
            int lose = result[1];
            graph[win][lose] = true; // win 선수가 lose 선수를 이김
        }
        
        // 플로이드-워셜
        for(int k = 1; k <= n; k++){
            for(int i = 1; i <= n; i++){
                for(int j = 1; j <= n; j++){
                    if(graph[i][k] && graph[k][j]){
                        graph[i][j] = true;
                    }
                }
            }
        }
        
        for(int i = 1; i <= n; i++){
            int count = 0;
            for(int j = 1; j <= n; j++){
                if(graph[i][j] || graph[j][i]){
                    count++;
                }
            }
            
            if(count == n-1){
                answer++;
            }
        }
        
        return answer;
    }
}
