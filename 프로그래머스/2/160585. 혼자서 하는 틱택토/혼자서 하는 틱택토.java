import java.util.*;

class Solution {
    public int solution(String[] board) {
                
        // Queue에 O, X 좌표 넣기
        Queue<int[]> Opos = new LinkedList<>();
        Queue<int[]> Xpos = new LinkedList<>();
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length(); j++) {
                char c = board[i].charAt(j);
                if(c == 'O') {
                    Opos.offer(new int[]{i, j});
                }
                if(c == 'X') {
                    Xpos.offer(new int[]{i, j});
                }
            }
        }
        
        // O-X 개수 >=2 , X개수-0개수 >= 1 차이 나진않는가
        int Ocount = Opos.size();
        int Xcount = Xpos.size();
        
        if(!(Ocount == Xcount || Ocount == Xcount + 1)) return 0;
    
        
        int placeCount = 0;
        // newBoard 초기화
        String[][] newBoard = new String[3][3];
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++){
                newBoard[i][j] = ".";
            }
        } 
        
        while(placeCount != Ocount + Xcount) { // 다 놓을 때 까지
            boolean Oturn = placeCount % 2 == 0 ? true : false; // O 놓을 차례인가
            
            if(Oturn) {
                int[] position = Opos.poll();
                int x = position[0];
                int y = position[1];
                newBoard[x][y] = "O";
            } else {
                int[] position = Xpos.poll();
                int x = position[0];
                int y = position[1];
                newBoard[x][y] = "X";
            }
            
            placeCount++;
            
            if(placeCount >= 3) {
                boolean Owin = isWin(newBoard, "O");
                boolean Xwin = isWin(newBoard, "X");
                
                if (Owin && Xwin) return 0;
                
                // O이 이미 이겼는데, X 놓을거 있는경우
                if (Owin && Ocount != Xcount + 1) return 0;
                // X가 이미 이겼는데, O 놓을거 있는경우
                if (Xwin && Ocount != Xcount) return 0;
                
            }
            
        }
        
        return 1;
    }
    
    
    public boolean isWin(String[][] newBoard, String turn) {
        
        // 열, 행 
        for(int i = 0; i < 3; i++) {
            if(newBoard[i][0].equals(turn) && newBoard[i][1].equals(turn) && newBoard[i][2].equals(turn)) {
                return true;
            }
            
            if(newBoard[0][i].equals(turn) && newBoard[1][i].equals(turn) && newBoard[2][i].equals(turn)) {
                return true;
            }
            
        }
        
        // 대각선
        if(newBoard[0][0].equals(turn) && newBoard[1][1].equals(turn) && newBoard[2][2].equals(turn)) {
            return true;
        }
        if(newBoard[2][0].equals(turn) && newBoard[1][1].equals(turn) && newBoard[0][2].equals(turn)) {
            return true;
        }
        
        
        return false;
    }
}