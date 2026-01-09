class Solution {
    public int solution(String s) {
        int answer = 0;
        
        char line = s.charAt(0);
        int count = 1;
        for(int i = 1; i < s.length(); i++) {
            if(count == 0) {
                System.out.println(s.charAt(i));
                answer++;
                line = s.charAt(i);
            }
            
            if(line == s.charAt(i)) {
                count++;
            } else {
                count--;
            }
            
        }
        
        // 마지막 +1
        answer++;
        
        return answer;
    }
}