class Solution {
    public int[] solution(int n) {
        int total = n * (n+1) / 2;
        
        int[] answer = new int[total];
        int[] step = new int[total];
        int startIndex = 0;
        for(int i = 1; i <= n; i++) {
            for(int j= startIndex; j < startIndex + i; j++){
                step[j] = i;
            }
            startIndex += i;
        }
        
        int markIndex = 0;
        int markNum = 2;
        answer[0] = 1;
        
        while(markNum <= total) {
            // 밑으로
            while(true){
                int nextIndex = markIndex + step[markIndex];
                if(nextIndex >= total){
                    break;
                }
                if(answer[nextIndex] != 0) { // 이미 채워져있다면
                    break;
                }
                
                answer[nextIndex] = markNum;
                markNum++;
                markIndex = nextIndex;
            }
            // System.out.println("1: " + markNum);
            // System.out.println("1번끝" + markIndex);
            // System.out.println(markIndex);
            // 옆으로
            while(true) {
                int nextIndex = markIndex + 1;
                if(nextIndex >= total){
                    break;
                }
                
                if(answer[nextIndex] != 0){
                    break;
                }
                
                answer[nextIndex] = markNum;
                markIndex = nextIndex;
                markNum++;
                
            }
            // System.out.println("2: " + markNum);
            
            // System.out.println(markIndex);
            // 위로 
            while(true) {
                int nextIndex = markIndex - step[markIndex];
                if(nextIndex < 0){
                    break;
                }
                if(answer[nextIndex] != 0){
                    break;
                }
                
                answer[nextIndex] = markNum;
                markIndex = nextIndex;
                markNum++;
            }
            //System.out.println("3: " + markNum);
            // System.out.println("마지막 idnex: " + markIndex);
            // markNum = total;
        }
        
        
        
        return answer;
    }
}