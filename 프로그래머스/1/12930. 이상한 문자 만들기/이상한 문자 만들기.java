class Solution {
    public String solution(String s) {
        String answer = "";
        int idx = 0;
        
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == ' '){
                idx = 0;
                answer += c;
            } else{
                answer += (idx % 2 == 0) ? Character.toUpperCase(c) : Character.toLowerCase(c);
                idx++;
            }
        }
        
        return answer;
    }
}