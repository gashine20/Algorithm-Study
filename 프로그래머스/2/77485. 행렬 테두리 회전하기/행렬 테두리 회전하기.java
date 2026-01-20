class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] map = new int[rows][columns];
        
        // 셋팅
        int count = 1;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < columns; j++){
                map[i][j] = count++; 
            }
        }
                
        int index = 0;
        for(int[] query : queries){
            int value = rotation(query, map);
            
            // print(map);
            answer[index++] = value;
        }
        
        return answer;
    }
    
    public int rotation(int[] query, int[][] map){
        int x1 = query[0];
        int y1 = query[1];
        int x2 = query[2];
        int y2 = query[3];
        
        int before = map[x1-1][y1-1];
        int minValue = before;
        int temp = 0;
        
        // 오른쪽
        for(int i = y1; i < y2; i++){
            temp = map[x1-1][i]; // 현재값
            map[x1-1][i] = before; // before값 저장
            before = temp; // before은 현재값 전값 저장
            minValue = Math.min(minValue, before);
        }
        
        // 아래
        for(int i = x1; i < x2; i++){
            temp = map[i][y2-1];
            map[i][y2-1] = before;
            before = temp;
            minValue = Math.min(minValue, before);
        }
        
        // 왼쪽        
        for(int i = y2-2; i >= y1; i--){
            temp = map[x2-1][i];
            map[x2-1][i] = before;
            before = temp;
            minValue = Math.min(minValue, before);
        }
        
        // 위
        for(int i = x2-1; i >= x1; i--){
            temp = map[i][y1-1];
            map[i][y1-1] = before;
            before = temp;
            minValue = Math.min(minValue, before);
        }
        
        // 첫번째 값
        map[x1-1][y1-1] = before;
        
        return minValue;
        
    }
    
    public void print(int[][] map){
        for(int i = 0; i < map.length; i++ ){
            for(int j = 0; j < map[0].length; j++){
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}