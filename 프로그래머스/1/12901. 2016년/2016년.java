class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int[] days = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31};
        String[] week = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
        int index = 5;
        
        // a월 b일과 1월 1일 날짜 차이
        int p = 1;
        int q = b;
        for (int i = 0; i < a-1; i++) {
            q += days[i];
        }
        int k = q - p;
                
        int remain = k % 7;
        answer = week[(index + remain) % 7];
        
        
        return answer;
    }
}