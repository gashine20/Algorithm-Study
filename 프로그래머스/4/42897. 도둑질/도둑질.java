import java.util.*;

class Solution {
    public int solution(int[] money) {
        int answer = 0;
        int n = money.length;
        
        int[] dp1 = new int[n];
        int[] dp2 = new int[n];
        
        // 첫번째 집 털어 -> 마지막 집 못털어
        dp1[0] = money[0];
        dp1[1] = Math.max(money[0], money[1]);
        for(int i = 2; i < n; i++){
            dp1[i] = Math.max(dp1[i-1], dp1[i-2] + money[i]);
        }
        
        // 첫번째집 x -> 마지막집 o
        dp2[0] = 0;
        dp2[1] = money[1];
        for(int i =2; i< n; i++){
            dp2[i] = Math.max(dp2[i-1], dp2[i-2] + money[i]);
        }
        
        answer = Math.max(dp1[n-2], dp2[n-1]);
        
        return answer;
    }
}