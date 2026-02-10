import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;

        // 1에서 각 N 위치까지 얼마나 걸리는 거리
        ArrayList<ArrayList<int[]>> graph = new ArrayList<>();
        for(int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        for(int[] r : road) {
            int a = r[0];
            int b = r[1];
            int c = r[2];
            graph.get(a).add(new int[]{b, c}); // a-> b c비용
            graph.get(b).add(new int[]{a, c});
        }
        
        int[] result = dijkstra(graph, 1, N);
        for(int a: result){
            if(a <= K) answer++;
        }
        
        return answer;
    }
    
    public int[] dijkstra(ArrayList<ArrayList<int[]>> graph, int start, int N){
        int[] dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            return o1[1] - o2[1];
        });
        pq.offer(new int[]{start, 0});
        dist[start] = 0;
        
        while(!pq.isEmpty()) {
            int[] now = pq.poll();
            int node = now[0];
            int cost = now[1];
            
            ArrayList<int[]> list = graph.get(node);
            for(int[] next : list) {
                int nextNode = next[0];
                int weight = next[1];
                
                if(weight >= dist[nextNode]) continue;
                
                if(cost+weight < dist[nextNode]) {
                    dist[nextNode] = cost+weight;
                    pq.offer(new int[]{nextNode, cost+weight});
                }
            }
        }
        // System.out.println(Arrays.toString(dist));
        return dist;
    }
}