import java.util.*;

class Solution {
    private int maxDiff = 0;
    private int[] best = new int[11];
    
    public int[] solution(int n, int[] info) {        
        dfs(n, info, new int[11], 0);
        
        if(maxDiff == 0) return new int[]{-1};
        
        return best;
    }
    
    public void dfs(int n, int[] info, int[] result, int nowIndex) {
        
        if(nowIndex == 11) { // 한 바퀴 다 돔
            if(n > 0) result[10] += n; // 남은 화살 몰아주기
            
            // System.out.println(Arrays.toString(result));

            // 1. 점수차이 계산
            int diff = calcScoreDiff(info, result);    
            if(diff > maxDiff) { // 최대 차이가 나면 result 반영
                maxDiff = diff;
                best = result.clone();
            } else if(diff == maxDiff && diff != 0) { // ** 점수가 같으면 낮은 점수를 더많이 맞힌 경우를 return
                if(isBetter(result, best)) {
                    best = result.clone();
                }
            }
            
            if(n>0) result[10] -= n; // 복구
            return;
        }
        
        // 1. nowIndex를 이기거나
        int apeachScore = info[nowIndex];
        if(apeachScore + 1 <= n) {
            result[nowIndex] = apeachScore + 1;
            dfs(n-result[nowIndex], info, result, nowIndex+1);
            result[nowIndex] = 0;
        }
        
        // 2. nowIndex를 안하거나
        dfs(n, info, result, nowIndex+1);
        
    }
    
    public int calcScoreDiff(int[] info, int[] result) {
        int diff = 0;
        
        int aScore = 0;
        int rScore = 0;
        for(int i = 0; i <= 10; i++) {
            if(info[i] < result[i]) {
                rScore += 10-i;
                continue;
            }
            if(info[i] != 0) {
                aScore += 10-i;
            }
        }
        
        // System.out.println("어피치: " + aScore + " 라이언:" + rScore);
        
        if(aScore > rScore) { // 어피치가 이겼으면 -1
            return -1;
        }
        
        return rScore - aScore;
    }
    
    public boolean isBetter(int[] result, int[] best) {
        for(int i = 10; i >= 0; i--) {
            if(result[i] > best[i]) return true;
            if(result[i] < best[i]) return false;
        }
        return false;
    }
}