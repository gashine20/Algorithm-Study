import java.util.*;

class Solution {
    boolean[][] visited;
    boolean[][] visited2;
    List<List<int[]>> emptyBlocks = new ArrayList<>();
    List<List<int[]>> blocks = new ArrayList<>();
    
    public int[][] turnLeft(int[][] board){
        int rows = board.length;
        int cols = board[0].length;
        int[][] newBoard = new int[cols][rows];
        
        for(int i = 0; i < cols; i++){
            for(int j = 0; j < rows; j++){
                newBoard[i][j] = board[j][cols - i - 1];
            }
        }
        return newBoard;
    }
    
    public boolean isCorrect(int[][] board, int[][] block){
        if(board.length != block.length || board[0].length != block[0].length) return false;

        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] != block[i][j]){
                    return false;
                }
            }
        }
        return true;
    }
    
    public boolean checkSame(int[][] board, int[][] block){
        // block을 돌려서 나온 모양이 board와 같은지 확인        
        if(isCorrect(board, block)){return true;}
        int[][] newBlock = block;
        
        for(int i = 0; i < 3; i++){
            newBlock = turnLeft(newBlock); // 시계 방향으로 바꿈
            if(isCorrect(board, newBlock)){return true;}
        }
        return false;
    }
    
    public void bfs(int n, int x, int y){
        List<int[]> list = new ArrayList<>();
        Queue<int[]> queue = new LinkedList<>();
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        queue.offer(new int[]{x, y});
        visited[x][y] = true;
        
        while(!queue.isEmpty()){
            int[] now = queue.poll();
            int nowX = now[0];
            int nowY = now[1];
            list.add(new int[]{nowX, nowY});
            
            for(int i = 0; i < 4; i++){
                int nx = nowX + dx[i];
                int ny = nowY + dy[i];
                
                if(nx >= 0 && nx < n && ny >= 0 && ny < n){
                    if(!visited[nx][ny]){
                        visited[nx][ny] = true;
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }    
        }
        emptyBlocks.add(list); // list = [[3,2], [4,1], [4,2], [4,3]]     
    }
    
    public void bfs2(int n, int x, int y){
        List<int[]> list = new ArrayList<>();
        Queue<int[]> queue = new LinkedList<>();
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        queue.offer(new int[]{x, y});
        visited2[x][y] = true;
        
        while(!queue.isEmpty()){
            int[] now = queue.poll();
            int nowX = now[0];
            int nowY = now[1];
            list.add(new int[]{nowX, nowY});
            
            for(int i = 0; i < 4; i++){
                int nx = nowX + dx[i];
                int ny = nowY + dy[i];
                
                if(nx >= 0 && nx < n && ny >= 0 && ny < n){
                    if(!visited2[nx][ny]){
                        visited2[nx][ny] = true;
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }    
        }
        blocks.add(list); // list = [[3,2], [4,1], [4,2], [4,3]]     
    }
    
    public int solution(int[][] game_board, int[][] table) {
        int answer = 0;
        int n = game_board.length;
        visited = new boolean[n][n];
        visited2 = new boolean[n][n];
        
        // game_board 초기화
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(game_board[i][j] == 1){
                    visited[i][j] = true;
                }
            }
        }
        // game_board 빈 공간 찾기
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(!visited[i][j]){
                    bfs(n, i, j);
                }
            }
        }
        
        // table 블록 초기화
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(table[i][j] == 0){
                    visited2[i][j] = true;
                }
            }
        }
        
        // blocks 찾기
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(!visited2[i][j]){
                    bfs2(n, i, j);
                }
            }
        }
        
        List<Block> findBlocks = new ArrayList<>();
        for(List<int[]> emptyBlock : emptyBlocks){
            Block block = new Block(emptyBlock);
            findBlocks.add(block);
        }
        
        List<Block> tableBlocks = new ArrayList<>();
        for(List<int[]> block : blocks){
            Block b = new Block(block);
            tableBlocks.add(b);
        }
        
        
        for(Block findBlock : findBlocks){
            for(int i = 0; i < tableBlocks.size(); i++){
                if(checkSame(findBlock.board, tableBlocks.get(i).board)){
                    //findBlock.printBoard();
                    
                    answer += findBlock.n;
                    tableBlocks.remove(i);
                    break;
                }
            }
        }
        
        return answer;
    }
    
    public class Block{
        int[][] board;
        int n;
        
        public Block(List<int[]> pos){
            this.board = makeNewBoard(pos);
            this.n = countBlock();
            
            //printBoard();
        }
        
        private int[][] makeNewBoard(List<int[]> pos){ // 최소 직사각형
            int minX = Integer.MAX_VALUE;
            int minY = Integer.MAX_VALUE;
            int maxX = Integer.MIN_VALUE;
            int maxY = Integer.MIN_VALUE;

            // 모든 수의 최대, 최소 구하고 새로운 board 길이 구하기
            // x 값 중에서 min 값, y 값 중에서 min 값 구하기
            for(int[] p : pos){
                int x = p[0];
                int y = p[1];

                minX = Math.min(minX, x);
                minY = Math.min(minY, y);
                maxX = Math.max(maxX, x);
                maxY = Math.max(maxY, y);
            }
            int rows = maxX - minX + 1;
            int cols = maxY - minY + 1;

            // 새로운 board 만들기
            int[][] newBoard = new int[rows][cols];

            for(int[] p : pos){
                int x = p[0] - minX;
                int y = p[1] - minY;
                newBoard[x][y] = 1;
            }

            return newBoard;
        
        }
        
        private int countBlock(){
            int count = 0;
            for(int i = 0; i < board.length; i++){
                for(int j = 0; j < board[i].length; j++){
                    if(board[i][j] == 1){
                        count++;
                    }
                }
            }
            return count;
        }
        
        public void printBoard(){
            for(int[] row : board){
                System.out.println(Arrays.toString(row));
            }
            System.out.println();
        }
    }
}