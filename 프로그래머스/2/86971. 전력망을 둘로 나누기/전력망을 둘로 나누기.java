import java.util.*;

class Solution {
    public int bfs(ArrayList<ArrayList<Integer>> graph, int start, boolean[] visited){
        int count = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        
        while(!queue.isEmpty()){
            int now = queue.poll();
            visited[now] = true;
            
            for(int next: graph.get(now)){
                if(!visited[next]){
                    queue.offer(next);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    
    public int countGap(ArrayList<ArrayList<Integer>> graph, int n){
        boolean[] visited = new boolean[n+1];
        int[] results = new int[2];
        int index = 0;
        
        //두 전력망 차이 계산
        for(int i = 1; i <= n; i++){
            if(!visited[i]){
                int result = bfs(graph, i, visited);
                results[index++] = result;
            }
        }
        
        return Math.abs(results[0]-results[1]);
    }
    
    
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        
        for(int i = 0; i < wires.length; i++){
            ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
            for (int p = 0; p <= n; p++) { // n+1 크기
                graph.add(new ArrayList<>());
            }
            
            for(int j = 0; j < wires.length; j++){
                if(i == j){continue;}
                graph.get(wires[j][0]).add(wires[j][1]);
                graph.get(wires[j][1]).add(wires[j][0]);
            }
            int result = countGap(graph, n);
            answer = Math.min(answer, result);
        }
        
        return answer;
    }
}