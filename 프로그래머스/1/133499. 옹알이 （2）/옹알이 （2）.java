class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] speaks = {"aya", "ye", "woo", "ma"};
        
        
        for(String b : babbling){
            if(b.contains("ayaaya") || b.contains("yeye") || b.contains("woowoo") || b.contains("mama")) {
                continue;
            }
            
            for(String speak : speaks){
                b = b.replace(speak, " ");
            }
            
            b = b.replace(" ", "");
            System.out.println(b);
            
            if(b.length() == 0){
                answer+=1;
            }
        }
        
        return answer;
    }
    
    
}