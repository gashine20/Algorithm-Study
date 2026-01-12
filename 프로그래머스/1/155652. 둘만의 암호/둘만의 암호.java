class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        
        String[] skips = skip.split("");
        
        for(char c : s.toCharArray()) {
            char decodedC = decode(skips, index, c);
            answer+=decodedC;
        }
        return answer;
    }
    
    public char decode(String[] skips, int index, char c) {
        char decodedC = c;
        int count = 0;
        int i = 1;
        // System.out.println(skips[0]);

        while(count != index) {
            decodedC = (char)((c - 'a' + i) % 26 + 'a');
            i++;
            
            boolean flag = false;
            for(String skip : skips){
                if(String.valueOf(decodedC).equals(skip)) {
                    flag = true;
                    break;
                } 
            }
        
            // System.out.println(decodedC);
            if(!flag){
                count++;
            }
        }
        
        return decodedC;
    }
}