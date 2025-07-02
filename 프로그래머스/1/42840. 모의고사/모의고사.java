import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] supo1 = new int[]{1,2,3,4,5};
        int[] supo2 = new int[]{2,1,2,3,2,4,2,5};
        int[] supo3 = new int[]{3,3,1,1,2,2,4,4,5,5};
        
        int[] correctCount = new int[]{0, 0, 0};
        
        for(int i = 0; i < answers.length; i++){
            int index1 = i % supo1.length;
            if(supo1[index1] == answers[i]){correctCount[0]++;}
            
            int index2 = i % supo2.length;
            if(supo2[index2] == answers[i]){correctCount[1]++;}
            
            int index3 = i % supo3.length;
            if(supo3[index3] == answers[i]){correctCount[2]++;}
        }
        
        
        int[] correctCountCopy = Arrays.copyOf(correctCount, correctCount.length);
        Arrays.sort(correctCountCopy);
        int maxCorrect = correctCountCopy[correctCount.length - 1];
        
        ArrayList<Integer> answerlist = new ArrayList<>();
        for(int i = 0; i < 3; i++){
            if(maxCorrect == correctCount[i]){
                answerlist.add(i+1);
            }
        }
        
        // covert arraylist to array
        int[] answer = answerlist.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}