import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = Integer.MAX_VALUE;
        int len = begin.length();
        if(!Arrays.asList(words).contains(target)){
            return 0;
        }
        
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        ArrayList<Integer> startIndex = new ArrayList<>();
        
        // begin과 알파벳 한 개 차이 나면 startIndex에 넣기
        for(int i = 0; i < words.length; i++){
            int count = 0;
            String word = words[i];
            for(int j = 0; j < len; j++){
                if(begin.charAt(j) == word.charAt(j)){
                    count++;
                }
            }
            if(count == len-1){
                startIndex.add(i);
            }
        }
        
        // words 인접 리스트 list 초기화
        for(int i = 0; i < words.length; i++){
            String now = words[i];
            ArrayList<Integer> linkedList = new ArrayList<>();
            
            for(int j = 0; j < words.length; j++){
                if(i == j){continue;}
                int count = 0;
                String next = words[j];
                for(int k=0; k < len; k++){
                    if(now.charAt(k) == next.charAt(k)){count++;}
                }
                if(count == len -1){
                    linkedList.add(j);
                }
            }
            list.add(linkedList);
        }
        
        for(int start: startIndex){ // begin부터 words로 변환할 수 있는 것부터 시작
            boolean[] visited = new boolean[words.length];
            
            int count = DFS(start, list, target, words, visited, 1);
            // System.out.println();
            // System.out.println("start:" + start + " count:" + count);
            answer = Math.min(answer, count);
        }
        if(answer == Integer.MAX_VALUE){
            return 0;
        }
        
        return answer;
    }
    
    public int DFS(int start, ArrayList<ArrayList<Integer>> list, String target, String[] words, boolean[] visited, int count){ 
        if(words[start].equals(target)){
            return count;
        }
        
        int minCount = Integer.MAX_VALUE;
        boolean foundPath = false;
        
        // System.out.print(start + "-> ");
        visited[start] = true;
        ArrayList<Integer> nexts = list.get(start);
        for(int next: nexts){
            if(!visited[next]){
                int result = DFS(next, list, target, words, visited, count+1);
                if(result>0){
                    minCount = Math.min(minCount, result);
                    foundPath = true;
                }
            }
        }
        
        visited[start] = false;
        
        return foundPath ? minCount : -1;
        
    }
    
}