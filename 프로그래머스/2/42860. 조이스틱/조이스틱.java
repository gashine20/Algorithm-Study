import java.util.*;

class Solution {
    public int solution(String name) {
        int answer = 0;
        
        
        // 위아래 알파벳 최소 변경
        for(char c : name.toCharArray()) {
            int result = alphaMove(c);
            answer+= result;
        }
        
        
        // 왼오 커서 위치 최소 변경
        // 1 ~ 10
        // 1          7 8 9
        // 1 -> 9 (2) + 9-> 8 + 8 -> 7 => 4
        // 1 -> 7 (6) + 7 -> 8 + 8 -> 9 => 8
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < name.length(); i++) {
            if(name.charAt(i) != 'A'){ // 'A'가 아니면
                list.add(i); // index값 list에 추가
            }
        }
        
        int count = positionMove(name);
        answer += count;
        
        
        return answer;
    }
    
    public int positionMove(String name) {
        // list = 1 7 8 9 
        int n = name.length();
        int move = n -1;
        
        for(int i = 0; i < n; i++) {
            int next = i +1;
            
            while(next < n && name.charAt(next)=='A') {
                next++;
            }
            
            // 오른쪽으로 갔다가 되돌아오기
            int case1 = i * 2 + (n - next);
            
            // 왼쪽 먼저 갔다가 오기
            int case2 = i + 2 * (n-next);
            
            move = Math.min(move, Math.min(case1, case2));
        }
        
        return move;
    }
    
    public int alphaMove(char c) {
        int A = 'A' - '0';
        int Z = 'Z' - '0';
        int C = c - '0';
        
        return Math.min(C-A, Z-C+1); // (오른쪽 , 왼쪽)
    }
}