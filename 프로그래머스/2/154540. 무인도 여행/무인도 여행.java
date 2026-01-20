import java.util.*;

class Solution {
    public int[] solution(String[] maps) {
        int r = maps.length;
        int c = maps[0].length();
        
        // String[] -> String[][]
        String[][] field = new String[r][c];
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++){
                field[i][j] = Character.toString(maps[i].charAt(j));
            }
        }
        
        boolean[][] visited = new boolean[r][c];
        ArrayList<Integer> result = new ArrayList<>();
        
        // for문 X 아니면 bfs
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(!field[i][j].equals("X") && !visited[i][j]){
                    int count = bfs(i, j, field, visited);
                    result.add(count);
                }
            }
        }
        
        // result size = 0
        if(result.isEmpty()){
            return new int[]{-1};
        }
            
        // 정렬
        Collections.sort(result);
        
        // list -> array
        int[] answer = result.stream()
            .mapToInt(Integer::intValue)
            .toArray();
        
        return answer;
    }
    
    
    public int bfs(int i, int j, String[][] field, boolean[][] visited){
        int count = 0;
        Queue<int[]> queue = new LinkedList<>();
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        // 초기화
        queue.add(new int[]{i, j});
        visited[i][j] = true;
        while(queue.size() > 0) {
            int[] a = queue.poll();
            int x = a[0];
            int y = a[1];
            count += Integer.parseInt(field[x][y]);
            
            for(int q = 0; q < 4; q++){
                int nx = x + dx[q];
                int ny = y + dy[q];
                
                if(nx >= 0 && nx < field.length && ny >= 0 && ny < field[0].length){
                    if(!field[nx][ny].equals("X") && !visited[nx][ny]){
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }
        
        
        return count;
    }
    
}