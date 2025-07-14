import java.util.*;

class Solution {
    public boolean checkPuddle(int[][] puddles, int i, int j){
        for(int[] puddle: puddles){
            if(i == puddle[1]-1 && j == puddle[0]-1){ // [x, y] → [j, i]
                return true;
            }
        }
        return false;
    }

    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m];
        int mod = 1_000_000_007;

        dp[0][0] = 1; // ✅ 출발점 초기화

        // 가로줄 초기화
        for (int j = 1; j < m; j++) {
            if (checkPuddle(puddles, 0, j)) break;
            dp[0][j] = 1;
        }

        // 세로줄 초기화
        for (int i = 1; i < n; i++) {
            if (checkPuddle(puddles, i, 0)) break;
            dp[i][0] = 1;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (checkPuddle(puddles, i, j)) continue;
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod;
            }
        }

        return dp[n - 1][m - 1];
    }
}
