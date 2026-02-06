import java.util.*;

class Solution {
    public double[] solution(int k, int[][] ranges) {
        
        // list = 5, 16, 8, 14, 2, 1
        ArrayList<Integer> list = new ArrayList<>();
        list.add(k); // 처음꺼
        while(k != 1) {
            if(k%2 == 0) { // 짝수면 2로 나눔
                k = k/2;
            } else { // 홀수면 3을 곱하고 1을 더함
                k = k * 3 + 1;
            }
            list.add(k);
        }
        
        // System.out.println(list);
        
        // 그래프 그려서 정적분
        int n = list.size();
        // System.out.println(n);
        
        double[] board = new double[n-1];
        for(int i = 0; i < n-1; i++) {
            int a = list.get(i);
            int b = list.get(i+1);
            
            int max = Math.max(a, b);
            // board = 16-((double)(16-5)/2) , 16-((double)(16-8)/2) ..
            // board[0] = [0,1] 거리
            board[i] = max - ((double)Math.abs(a-b)/2);
        }
        
        
        // System.out.println(Arrays.toString(board));
        
        // 구간에 맞게 정적분 결과목록 리턴
        double[] answer = new double[ranges.length];
        for(int i = 0; i < ranges.length; i++) {
            int a = ranges[i][0];
            int b = n+ranges[i][1]-1;
            
            if(a == b) { // [2,-3] = [2, 5-3] = 0
                answer[i] = 0.0;
                continue;
            }
            
            if(a > b) { // [3, -3] = [3, 2] = -1
                answer[i] = -1.0;
                continue;
            }
            
            // [2, -1] = [2, 5-1] = [2,4] = board[4] - board[2];
            for(int j = a; j < b; j++) {
                answer[i] += board[j];
            }
        }
        
        
        return answer;
    }
}