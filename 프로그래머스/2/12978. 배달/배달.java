import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        int[] distance = new int[N+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[1] = 0;
        
        ArrayList<ArrayList<int[]>> list = new ArrayList<>();
        
        for(int i = 0; i <= N; i++){
            list.add(new ArrayList<>());
        }
        
        for(int i = 0; i < road.length; i++){
            int a = road[i][0];
            int b = road[i][1];
            int c = road[i][2];
            
            list.get(a).add(new int[]{b,c});
            list.get(b).add(new int[]{a,c}); 
        }
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        pq.offer(new int[]{1,0});
        
        while(!pq.isEmpty()) {
            int[] arr = pq.poll();
            int now = arr[0];
            int dist = arr[1];
            
            if(distance[now] < dist) continue;
            
            for(int[] nextArr : list.get(now)){
                int next = nextArr[0];
                int cost = nextArr[1];
                
                if(distance[next]  > distance[now] + cost){
                    distance[next] = distance[now] + cost;
                    pq.offer(new int[]{next, distance[next]});
                }
            }
        }
        
        
        // K 이하 개수 세기
        for(int i = 1; i < distance.length; i++){
            System.out.println(distance[i]);
            if(distance[i] <= K){
                answer++;
            }
        }

        return answer;
    }
}