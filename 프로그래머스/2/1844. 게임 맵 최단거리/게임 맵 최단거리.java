import java.util.*;

class Solution {
    public int solution(int[][] maps) {        
        // dp 로도 풀 수 있는데
        int answer = bfs(maps);
        
        return answer;
    }
    
    public int bfs(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> queue = new LinkedList<>();
        
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        queue.offer(new int[]{0, 0, 1});
        visited[0][0] = true;
        
        while(!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0];
            int y = now[1];
            int c = now[2];
            
            if(x == n-1 && y == m-1) { // 도착
                return c;
            }
            
            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if(maps[nx][ny]== 1 && !visited[nx][ny]) { // 길이고, 방문한적없으면
                        queue.offer(new int[]{nx, ny, c+1});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
        
        return -1;
        
        
    }
}