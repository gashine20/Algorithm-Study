import java.util.*;

class Solution {
    public int solution(String name) {
        int answer = 0;
        int len = name.length();
        int move = name.length()-1; // 기본 최소 오왼이동
        for(int i = 0; i < len; i++){
            // 위/아래 알파벳 최소 변경
            answer += Math.min(name.charAt(i) - 'A', 'Z'-name.charAt(i)+1);
            
            // 'A'가 끝나는 지점 찾기
            int next = i+1;
            while(next < len && name.charAt(next) == 'A'){
                next++;
            }
            
            // 좌우이동 최소 구하기
            move = Math.min(move, (i*2) + len - next);
            move = Math.min(move, (len-next)*2 +i);         
        }
        
        answer += move;
        
        return answer;
    }
}

//"JAN" 첫번째에서 위9, 왼쪽1, 위13 = 총 23
// B~N 위 1~13 Z~M 아래 1~13
// 커서 이동 - 오/왼 갈지

// "JABB" 위9, 왼쪽1, 위1, 왼쪽1, 위1 = 13
// 또는 위9, 오2 위1 오1 위1 = 14

// 오,왼 커서 이동 따로 - {1,1,0,0,1} 이면 움직임3, 
// 항상, 1에서 3으로 가야하는 지금, 

// 알파벳 변경 따로 - 고정된값