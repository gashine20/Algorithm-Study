import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;
        
        for(int q = 0; q < wires.length; q++){
            // 초기화
            ArrayList<ArrayList<Integer>> list = new ArrayList<>();
            for(int i = 0; i <= n; i++){
                list.add(new ArrayList<>());
            }
            boolean[] visited = new boolean[n+1];
            
            for(int j = 0; j < wires.length; j++){
                if(q == j){
                    continue;
                }
                
                // 값 부여
                int x = wires[j][0];
                int y = wires[j][1];

                list.get(x).add(y);
                list.get(y).add(x);
                
            }
                        
            // bfs
            int result = bfs(1, list, visited);
            int diff = Math.abs(result - (n-result));            
                
            answer = Math.min(answer, diff);
        }
        

        return answer;
    }
    
    public int bfs(int start, ArrayList<ArrayList<Integer>> list, boolean[] visited){
        int count = 1;
        Queue<Integer> queue = new LinkedList<>();
        
        queue.add(start);
        visited[start] = true;
        
        while(queue.size()>0){
            int now = queue.poll();
            
            for(int next: list.get(now)){
                if(!visited[next]){
                    queue.add(next);
                    count+=1;
                    visited[next] =true;
                }
            }
        }

        return count;
    }
}