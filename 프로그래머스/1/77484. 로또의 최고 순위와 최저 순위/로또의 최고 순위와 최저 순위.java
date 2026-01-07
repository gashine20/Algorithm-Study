class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] rank = {6,6,5,4,3,2,1};
        
        int zeroCount = 0;
        int correctCount = 0;
        for(int lotto: lottos){
            if(lotto == 0){
                zeroCount += 1;
            } else {
                // 포함되어있는지 확인
                for(int num : win_nums){
                    if(num == lotto){
                        correctCount+=1;
                        break;
                    }
                }
            }
        }

        int[] answer = {rank[correctCount + zeroCount], rank[correctCount]};
        
        return answer;
    }
}