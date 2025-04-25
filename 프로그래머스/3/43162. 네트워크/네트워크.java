import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        boolean[] visited = new boolean[n];
        
        // 값 넣기
        for(int i = 0; i < n; i++){
            ArrayList<Integer> nexts = new ArrayList<>();
            for(int j = 0; j < n; j++){
                if(computers[i][j] == 1){
                    nexts.add(j);
                }
            }
            list.add(nexts);
        }
        
        
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                BFS(i, list, visited);
                answer += 1;
            }
        }
        return answer;
    }
    
    public void BFS(int start, ArrayList<ArrayList<Integer>> list, boolean[] visited){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        
        while(!queue.isEmpty()){
            int now = queue.poll();
            visited[now] = true;
            
            ArrayList<Integer> nexts = list.get(now);
            for(int next: nexts){
                if(!visited[next]){
                    queue.add(next);
                }
            }
        }
    }
    
}