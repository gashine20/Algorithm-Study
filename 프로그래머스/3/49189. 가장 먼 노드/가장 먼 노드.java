import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        List<List<Integer>> graph = new ArrayList<>();

        for(int i = 0; i < n+1; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] v : edge){
            int s = v[0];
            int e = v[1];
            
            graph.get(s).add(e);
            graph.get(e).add(s);
        }
                
        int[] dis = new int[n+1];
        for(int i = 2; i < n+1; i++){
            dis[i] = Integer.MAX_VALUE;
        }
        dis[0] = 0;
        
        //bfs
        boolean[] visited = new boolean[n+1];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        visited[1] = true;
        
        while(queue.size() > 0){
            int now = queue.poll();
            
            for(int next: graph.get(now)){
                if(!visited[next]){
                    visited[next] = true;
                    dis[next] = dis[now] + 1;
                    queue.offer(next);
                }
            }
        }
        
        Arrays.sort(dis);
        int max_distance = dis[n];
        for(int i = 2; i <= n; i++){
            if(dis[i] == max_distance){
                answer = n - i + 1;
                break;
            }
        }
        
        return answer;
    }
}