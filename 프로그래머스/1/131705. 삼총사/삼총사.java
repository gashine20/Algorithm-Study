import java.util.*;

class Solution {
    static List<int[]> list = new ArrayList<>();
    
    public int solution(int[] number) {
        int answer = 0;
        boolean[] visited = new boolean[number.length];
        combination(number, visited, 0, number.length, 3);
        
        for(int[] pick : list){
            if(Arrays.stream(pick).sum() == 0){
                answer +=1;
            }
        }
        
        return answer;
    }
    
    public void combination(int[] number, boolean[] visited, int start, int n, int r){
        if(r == 0){
            int[] pick = new int[3];
            int idx = 0;
            for(int i = 0; i < n; i++){
                if (visited[i]) {
                    pick[idx++] = number[i];
                }
            }
            list.add(pick);
            return;
        }
        
        for(int i = start; i < n; i++){
            visited[i] = true;
            combination(number, visited, i+1, n, r-1);
            visited[i] = false;
        }
    }
}