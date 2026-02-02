import java.util.*;

class Solution {
    public int solution(String[] maps) {
        // 시작지점, 레버, exit 찾기
        Pos start = new Pos();
        Pos lev = new Pos();
        Pos exit = new Pos();
        
        for(int i = 0; i < maps.length; i++){
            for(int j = 0; j < maps[i].length(); j++){
                if(maps[i].charAt(j) == 'S'){
                    start = new Pos(i, j, 0);
                } else if(maps[i].charAt(j) == 'L') {
                    lev = new Pos(i, j, 0);
                } else if(maps[i].charAt(j) == 'E') {
                    exit = new Pos(i, j, 0);
                }
            }
        }
        
        
        // 시작지점 -> 레버
        int d1 = bfs(maps, start, lev);
        if(d1 == -1) return -1;
            
        // 레버 -> exit 
        int d2 = bfs(maps, lev, exit);
        if(d2 == -1) return -1;

        return d1 + d2;
    }
    
    public int bfs(String[] maps, Pos start, Pos end){
        Queue<Pos> queue = new LinkedList<>();
        int n = maps.length;
        int m = maps[0].length();
        boolean[][] visited = new boolean[n][m];
        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};
        
        queue.add(start);
        visited[start.x][start.y] = true;
        
        while(!queue.isEmpty()){
            Pos now = queue.poll();
            int x = now.x;
            int y = now.y;
            // System.out.println(now.x + " " + now.y);
            
            if(now.x == end.x && now.y == end.y){ // 도착하면
                return now.dist;
            }
            
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(nx >= 0 && nx < n && ny >=0 && ny < m){
                    if(!visited[nx][ny] && maps[nx].charAt(ny) != 'X'){
                        visited[nx][ny] = true;
                        queue.add(new Pos(nx, ny, now.dist + 1));
                    }
                }
            }
            
        }
        
        return -1;
        
    }
    
    
    
    public class Pos {
        int x;
        int y;
        int dist;
        
        public Pos(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
        
        public Pos() {
        }
    }
}