import java.util.*;

class Solution {
    static int[] parent;
    
    public int find(int a){
        if(a == parent[a]){
            return a;
        } else{
            parent[a] = find(parent[a]);
            return parent[a];
        }    
    }
    
    public void union(int a, int b){ // parent b에 a를
        int aParent = find(a);
        int bParent = find(b);
        if(aParent != bParent){
            parent[bParent] = aParent;
        }
    }
    
    public int solution(int n, int[][] costs) {
        int answer = 0;
        // MST
        parent = new int[n];
        for(int i = 0; i < n; i++){
            parent[i] = i;
        }
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        for(int i = 0; i < costs.length; i++){
            int s = costs[i][0];
            int e = costs[i][1];
            int w = costs[i][2];
            
            pq.offer(new int[]{w,s,e});
        }
        
        int useEdge = 0;
        while(useEdge < n-1){
            int[] node = pq.poll();
            int w = node[0];
            int a = node[1];
            int b = node[2];
            
            if(find(a) != find(b)){
                union(a,b);
                answer += w;
                useEdge++;
            }   
        }
        
        return answer;
    }
}