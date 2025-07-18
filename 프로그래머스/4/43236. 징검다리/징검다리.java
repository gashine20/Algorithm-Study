import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        Arrays.sort(rocks);
        
        int left = 1;
        int right = distance;
        while(left <= right){
            int mid = (left + right) / 2;
            int before = 0;
            int end = distance;
            int delete = 0;
            
            for(int rock : rocks){
                int dis = rock - before;
                if(dis < mid){
                    delete++;
                    continue;
                } 
                before = rock;
            }
            // 마지막
            if(end - before < mid){delete++;}
            
            if(delete <= n){ // 범위를 줄여야함
                left = mid + 1;
                answer = mid;
            } else{
                right = mid - 1;
            }
        }
        
        return answer;
    }
}