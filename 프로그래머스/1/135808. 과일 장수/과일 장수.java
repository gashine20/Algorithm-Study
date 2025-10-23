import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        // 최대 k점, m개 상자에 담음
       score = Arrays.stream(score)
           .boxed()
           .sorted(Collections.reverseOrder())
           .mapToInt(Integer::intValue)
           .toArray();

        for(int i = 0; i < score.length/m; i++){
            int[] arr = Arrays.copyOfRange(score,i*m, i*m+m);
            int minValue = Arrays.stream(arr).min().getAsInt();
            answer += minValue * m;
        }
        return answer;
    }
}