class Solution {
    public int solution(int n) {
        int answer = 0;
        
        boolean[] row = new boolean[n]; // 행
        boolean[][] board = new boolean[n][n];
        
        for(int i = 0; i < n; i++) { // 첫번째 열 기준으로 
            row[i] = true;
            board[i][0] = true;
            answer+= dfs(row, board, 1);
            row[i] = false;
            board[i][0] = false;
        }
        
        return answer;
    }
    
    
    public int dfs(boolean[] row, boolean[][] board, int now_col) {
        int result = 0;
        int n = row.length;
        
        if(now_col == n) { // 마지막까지 다 왔다면
            return 1;
        }
        
        // 현재 탐색할 열은 now_col
        for(int i = 0; i < n; i++) {
            if(!row[i]){ // 가로나 세로에 Q 없는지 확인
                // 없으면 대각선에도 없는 지 확인
                if(checkPosition(i, now_col, board)){
                    row[i] = true;
                    board[i][now_col] = true;
                    // System.out.println(i +"," + now_col);
                    result += dfs(row, board, now_col+1);
                    row[i] = false;
                    board[i][now_col] = false;
                }
            }
        }
        
        
        return result;
    }
    
    public boolean checkPosition(int x, int y, boolean[][] board){
        int[] dx = {1,1, -1, -1};
        int[] dy = {1, -1, 1, -1};
        int n = board.length;
        
        // (i, j) 대각선에 Q있는지 확인
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            while(nx >= 0 && nx < n && ny >=0 && ny < n) {
                if(board[nx][ny]) return false; // 대각선에 퀸 있음
                nx += dx[i];
                ny += dy[i];
            }
        }
        return true;
    }
}
