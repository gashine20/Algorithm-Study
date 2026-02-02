import java.util.*;

class Solution {
    public int solution(int[] cards) {
        int answer = 0;
        ArrayList<Integer> list = new ArrayList<>();
        
        // 하나씩 돌려서 영역 만들고오기
        int n = cards.length;
        boolean[] visited = new boolean[n];
        
        int count = 0;
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                count = dfs(cards, i, visited, 0);
                // System.out.println(count);
                list.add(count);
            }
        }
        
        if(list.size() <= 1){
            return 0;
        } 
        Collections.sort(list, Collections.reverseOrder());
        
        return list.get(0) * list.get(1);
    }
    
    public int dfs(int[] cards, int nowIndex, boolean[] visited, int count) {        
        if(visited[nowIndex]) { // 이미 열려있는 상자를 만날 때
            return count;
        }
        
        visited[nowIndex] = true;
        
        int nextIndex = cards[nowIndex] - 1;
        
        return dfs(cards, nextIndex, visited, count + 1);
    }
}