import java.util.*;

class Solution {
    public void printMap(int[][] maps){
        for(int[] map : maps){
            System.out.println(Arrays.toString(map));
        }
        
        System.out.println();
    }
    
    public int solution(int[][] maps) {
        int answer = 0;
        int n = maps.length;
        int m = maps[0].length;
        
        int[] nx = {1, -1, 0, 0};
        int[] ny = {0, 0, 1, -1};
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(maps[i][j] == 1){
                    maps[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        maps[0][0] = 1;

        queue.offer(new int[]{0,0});
        visited[0][0] = true;
        while(!queue.isEmpty()){
            int[] pos = queue.poll();
            int x = pos[0];
            int y = pos[1];
            
            for(int i = 0; i < 4; i++){
                int dx = x + nx[i];
                int dy = y + ny[i];
                
                if(dx < n && dx >=0 && dy < m && dy >=0){
                    if(maps[dx][dy] != 0 && !visited[dx][dy]){
                        maps[dx][dy] = Math.min(maps[dx][dy] ,maps[x][y] + 1);
                        queue.offer(new int[]{dx,dy});
                        visited[dx][dy] = true;
                    }
                }
            }
            
            //printMap(maps);
        }
        
        if(maps[n-1][m-1] == Integer.MAX_VALUE){
            return -1;
        }
        
        answer = maps[n-1][m-1];
        return answer;
    }
}