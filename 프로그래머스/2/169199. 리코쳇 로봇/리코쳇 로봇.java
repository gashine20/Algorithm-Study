import java.util.*;

class Solution {
    public int solution(String[] board) {        
        // R, G 찾기
        int[] start = new int[3];
        int[] end = new int[3];
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length(); j++) {
                if(board[i].charAt(j) == 'R'){
                    start[0] = i;
                    start[1] = j;
                    start[2] = 0;
                }
                if(board[i].charAt(j) == 'G'){
                    end[0] = i;
                    end[1] = j;
                    end[2] = 0;
                }
            }
        }
        
        int answer = bfs(start, end, board);
        return answer;
    }
    
    public int bfs(int[] start, int[] end, String[] board){
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        boolean[][] visited = new boolean[board.length][board[0].length()];
        Queue<int[]> queue = new LinkedList<>();
        int count = Integer.MAX_VALUE;
        
        queue.add(start);
        visited[start[0]][start[1]] = true;
        
        while(!queue.isEmpty()) {
            int[] now = queue.poll();
            
            if (now[0] == end[0] && now[1] == end[1]) {// end 도착
                count = Math.min(count, now[2]); // 최소 이동
                break;
            } 
            
            for(int i = 0; i < 4; i ++) {
                int[] next = find_pos(now, dx[i], dy[i], board);
                // System.out.println(Arrays.toString(next));
                if(!visited[next[0]][next[1]]){
                    visited[next[0]][next[1]] = true;
                    queue.add(next);
                }
            }
        }
        
        if(count == Integer.MAX_VALUE){
            count = -1;
        }
        return count;
        
    }
    
    public int[] find_pos(int[] now, int dx, int dy, String[] board){
        int[] next = new int[3];
        int x = now[0];
        int y = now[1];

        int nx = x;
        int ny = y;

        while (true) {
            int tx = nx + dx;
            int ty = ny + dy;

            if (tx < 0 || tx >= board.length || ty < 0 || ty >= board[0].length()) { // 벽
                break;
            }

            if (board[tx].charAt(ty) == 'D') { // 장애물
                break;
            }

            nx = tx;
            ny = ty;
        }

        next[0] = nx;              
        next[1] = ny;
        next[2] = now[2] + 1;

        return next;
    }   
}