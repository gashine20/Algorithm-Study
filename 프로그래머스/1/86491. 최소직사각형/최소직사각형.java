import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int[] minbox = new int[sizes.length];
        int[] maxbox = new int[sizes.length];
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for(int i = 0; i < sizes.length; i++){
            Arrays.sort(sizes[i]);
            minbox[i] = sizes[i][0];
            maxbox[i] = sizes[i][1];
        }
        
        Arrays.sort(minbox);
        Arrays.sort(maxbox);
        answer = minbox[sizes.length-1] * maxbox[sizes.length-1];
        
        return answer;
    }
}