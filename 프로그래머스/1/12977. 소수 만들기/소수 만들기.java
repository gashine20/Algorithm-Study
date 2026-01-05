import java.util.*;

class Solution {
    int answer = 0;
    
    public int solution(int[] nums) {
        dfs(0, 0, 0, nums);
        
        return answer;
    }
    
    public void dfs(int start, int depth, int total, int[] nums) {
        System.out.println(start +" " + depth + " " + total);
        if(depth == 3){
            if(isPrime(total)) {
                answer += 1;
                System.out.println(total);
            }
            return;
        }
        
        for (int i = start; i < nums.length; i++) {
            dfs(i+1, depth+1, total+nums[i], nums);
            
        }
    }
    
    public boolean isPrime(int totalSum) {
        // totalSum은 최소 3이상
        for(int i = 2; i <= Math.sqrt(totalSum) + 1; i++) {
            if(totalSum % i == 0) {
                return false;
            }
        }
        return true;
    }
    
}