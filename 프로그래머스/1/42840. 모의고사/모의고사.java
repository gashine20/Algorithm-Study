import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> answerList = new ArrayList<>();
        
        ArrayList<int[]> supojas = new ArrayList<>();
        supojas.add(new int[]{1,2,3,4,5});
        supojas.add(new int[]{2,1,2,3,2,4,2,5});
        supojas.add(new int[]{3,3,1,1,2,2,4,4,5,5});
        
        int correctAnswer = 0;
        int index = 1;
        for(int[] supoja : supojas){
            int count = 0;
            for(int i = 0; i < answers.length; i++ ){
                if(answers[i] == supoja[i%supoja.length]){
                    count+=1;
                }
            }
            if(correctAnswer < count) {
                answerList.clear();
                answerList.add(index);
                correctAnswer = count;
            } else if (correctAnswer == count) {
                answerList.add(index);
            }
                
            index +=1;
        }
        
        // 형 변환
        int[] answer = answerList.stream()
            .mapToInt(Integer::intValue)
            .toArray();
        
        return answer;
    }
}