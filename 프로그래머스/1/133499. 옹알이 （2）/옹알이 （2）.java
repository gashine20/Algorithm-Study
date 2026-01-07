class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] speaks = {"aya", "ye", "woo", "ma"};
        
        
        for(String b : babbling){
            int correctLen = 0;
            int beforeIndex = -1;
            
            while(correctLen != b.length()) {
                int newIndex = -1;
                // System.out.print(b + "- ");
                
                newIndex = isCorrect(b.substring(correctLen,b.length()), speaks, beforeIndex);

                
                System.out.println(newIndex);
                if(newIndex == -1){
                    // 맞는 단어가 없음
                    break;
                }
                correctLen += speaks[newIndex].length();
                beforeIndex = newIndex;
            }
            if(correctLen == b.length()) answer+=1;
            
        }
        
        return answer;
    }
    
    public int isCorrect(String b, String[] speaks, int beforeIndex){
        int newIndex = -1; // "aya" "ayaye" -> "aya" -> 0 , -1
        for(int i = 0; i < speaks.length; i++) {
            int endIndex = Math.min(speaks[i].length(),b.length());
            String cutString = b.substring(0, endIndex);
            
            System.out.println(cutString);
        
            if(beforeIndex != i && cutString.equals(speaks[i])){
                return i;
            }
        }
        return newIndex;
    }
}