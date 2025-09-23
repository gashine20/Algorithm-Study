class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int len = p.length();
        long intP = Long.parseLong(p);
        
        for(int i = 0; i < t.length()-len+1; i++){
            String str = t.substring(i, i+len);
            
            if(Long.parseLong(str) <= intP){
                answer++;
            }
        }
        
        return answer;
    }
}