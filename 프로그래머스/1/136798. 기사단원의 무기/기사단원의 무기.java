import java.util.*;

class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        for(int i = 1; i <= number; i++) {
            int count = countYakSu(i);
            if(count <= limit) {
                answer += count;
            } else {
                answer += power;
            }
        }
        return answer;
    }
    
    
    public int countYakSu(int num){
        if(num == 1) {
            return 1;
        }
        if(num == 2) {
            return 2;
        }
        
        int count = 1;
        for (int i = 2; i < Math.sqrt(num); i++ ){
            if(num % i == 0) {
                count +=1;
            }
        } 
        
        if(num % Math.sqrt(num) == 0) {
            return count*2 + 1;
        }
        return count*2;
    }
}