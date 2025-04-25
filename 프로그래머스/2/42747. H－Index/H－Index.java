import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        Arrays.sort(citations);
        int len = citations.length;
        int max = citations[len-1];
            
        for(int h = 0; h <= max; h++){
            int q = 0; // h번 이상 인용된 논문 개수
            int p = 0; // h번 미만 인용된 논문 개수
            boolean success = true;
            
            // [0, 1, 3, 5, 6]
            for(int j = 0; j < len; j++){
                // System.out.println("h: " + h + " 현재 값: " + citations[j]);
                
                if(citations[j] >= h){ // 인용
                    q+=1;
                } else{
                    p+=1;
                }
                
                // System.out.println("인용 수:" + q + " 인용 안된 수: " + p);
                if(p > h){ // h번 미만 인용된 논문 개수가 h보다 클 때
                    success = false;
                }
                
            }
            if(p <= h && q >= h && success){
                answer = h;
            }
        }
        return answer;
    }
}