import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        ArrayList<long[]> points = new ArrayList<>();
        
        // 교점을 알려주는 함수 
        long minX = Long.MAX_VALUE;
        long maxX = Long.MIN_VALUE;
        long minY = Long.MAX_VALUE;
        long maxY = Long.MIN_VALUE;
        
        for(int i = 0; i < line.length-1; i++) {
            for(int j = i+1; j < line.length; j++) {
                long[] point = findPoint(line[i], line[j]);
                if(point.length == 2){
                    // System.out.println(Arrays.toString(point));
                    // X, Y 최대 최소 구하기
                    minX = Math.min(minX, point[0]);
                    maxX = Math.max(maxX, point[0]);
                    minY = Math.min(minY, point[1]);
                    maxY = Math.max(maxY, point[1]);
                    
                    points.add(point);
                }
                
            }
        }
        
        int N = (int)(maxX - minX);
        int M = (int)(maxY - minY);
            
        String[] board = new String[M+1];
        StringBuilder sb = new StringBuilder();
        
        // . 초기화
        for(int i = 0; i <=M; i ++) {
            for(int j = 0; j <= N; j++) {
                sb.append(".");
            }
            board[i] = sb.toString();
            sb.delete(0, N+1);
        }
        
        // list에서 빼서 * 기입
        // x: 현재 좌표에서 - minX
        // y : maxY - 현재 좌표
        for(long[] point : points) {
            int x = (int)(point[0] - minX);
            int y = (int)(maxY - point[1]);
            
            // System.out.println(y + "," + x + "칠함");
            // *로 삽입
            StringBuilder sb2 = new StringBuilder(board[y]);
            sb2.setCharAt(x, '*');
            board[y] = sb2.toString();
        }
        
        
        return board;
    }
    
    public long[] findPoint(int[] line1, int[] line2) { // 정수 교점만 찾기
        long A = (long)line1[0], B=(long)line1[1], E=(long)line1[2];
        long C = (long)line2[0], D=(long)line2[1], F=(long)line2[2];
        
        if(A*D - B*C == 0){ // 평행하면 빈 int[] return
            return new long[]{};
        }
        
        long x = 0;
        long y = 0;
        if((B*F - E*D) % (A*D - B*C) != 0) {
            return new long[]{};
        }
        if((E*C - A*F) % (A*D - B*C) != 0) {
            return new long[]{};
        }
        x = (B*F - E*D) / (A*D - B*C);
        y = (E*C - A*F) / (A*D - B*C);
        
        return new long[]{x, y}; 
    }
}