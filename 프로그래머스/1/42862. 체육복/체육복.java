import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] people = new int[n];
        int answer = n;

        // 체육복 없음 -1, 체육복 있음 0, 여분 있음 1
        for (int l : lost) 
            people[l-1]--;
        for (int r : reserve) 
            people[r-1]++;
        
        // 체육복 없는 사람 입장에서 왼쪽꺼 먼저 스캔
        for(int i = 0; i < people.length; i++) {
            if (people[i] == -1) {
                // 왼쪽
                if (i-1 >= 0 && people[i-1] == 1) {
                    people[i-1] --;
                    people[i]++;
                } else if (i+1 < people.length && people[i+1] == 1) { // 오른쪽
                    people[i+1] --;
                    people[i]++;
                } else{ // 양 옆 둘다 여분없음
                    answer--;
                }
            }
        }
        
        return answer;
    }
}