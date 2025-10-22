class Solution {
    public String solution(int[] food) {
        String answerA = "";
        
        for(int i = 1; i < food.length; i++) {
            for(int j = 1; j <= food[i]/2; j++){
                answerA = answerA.concat(Integer.toString(i));
            }
        }
        
        StringBuilder sb = new StringBuilder(answerA);
        String answerB = sb.reverse().toString();
        
        String answer = answerA.concat("0").concat(answerB);
        
        return answer;
    }
}