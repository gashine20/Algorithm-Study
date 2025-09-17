class Solution {
    public long solution(int price, int money, int count) {
        long totalPrice = 0;
        
        for(int i = 1; i <= count; i++){
            totalPrice += (long) price * i;
        }
    
        long answer = totalPrice - money;
        if(answer < 0){
            return 0;
        }
        return answer;
    }
}